from machine import Pin


class Relay:
    #Pin value in relay:
    #1 = apagado
    #0 = encendido
    def __init__(self, pinNum, inverted=True, verbose=False):
        self.pin = Pin(pinNum, Pin.OUT)
        self.inverted = inverted
        self.verboseState = verbose
    
    def verbose(self):
        if self.verboseState:
            print(f"{self.pin} -> {self.pin.value()}")
    
    def on(self):
        if self.pin.value() == 1:
            self.pin.value(False if self.inverted else True)
            self.verbose()

    
    def off(self):
        if self.pin.value() == 0:
            self.pin.value(True if self.inverted else False)
            self.verbose()

    
    def getState(self):
        return self.pin.value()
    
    
