import random, asyncio, time
import machine, onewire, ds18x20
from tempLog import tempLog
from relayController import Relay

UMBRAL_TEMP = 28
PIN_RELAY = 5
PIN_SENSOR = 4
LOG_TEMP_TIME = 2


def getTemperature(pinSensor):
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(machine.Pin(pinSensor)))
    roms = ds_sensor.scan()

    ds_sensor.convert_temp()
    time.sleep_ms(750)
    
    return ds_sensor.read_temp(roms[0])


async def logTemperature(log):
    while True:
        log.addData(getTemperature(PIN_SENSOR))
        await asyncio.sleep(LOG_TEMP_TIME)


async def main():
    log = tempLog()
    asyncio.create_task(logTemperature(log))
    
    r0 = Relay(PIN_RELAY)
    r0.off()
    
    
    while True:
        print(f"{log.getData()} --> {log.getDataAvg()}")
        if log.getDataAvg() < UMBRAL_TEMP:
            r0.on()
        else:
            r0.off()
        
        await asyncio.sleep(LOG_TEMP_TIME)
        
        
        

try:
    asyncio.run(main())
except:
    r0.off()