class tempLog():
    def __init__(self, dataLen=5):
        self.tempData = []
        self.dataLen = dataLen
    
    def getData(self):
        if len(self.tempData) > 0:
            return self.tempData
        return 0


    def getDataAvg(self):
        
        try:
            return sum(self.tempData) / len(self.tempData)
        except:    
            return 0

    def addData(self, data):
        if len(self.tempData) >= self.dataLen:
            self.tempData.pop(0)
            
        self.tempData.append(data)
