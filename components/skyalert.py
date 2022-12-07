import requests

class SkyAlert():
    def __init__(self, address='http://192.168.1.2:81') -> None:
        self.address = address

    def getList(self):
        return requests.get(self.address).text.split()

    def getAmbientTemperature(self) -> float:
        # Unit: Degree C
        x = self.getList()
        return float(x[1])
    
    def getSkyTemperature(self) -> float:
        # Unit: Degree C
        x = self.getList()
        return float(x[2])

    def getDampnessValue(self) -> float:
        # x > 990 : dry
        # 990 > x > 970 : damp
        # 970 > x : wet
        x = self.getList()
        return float(x[3])

    def getBrightnessValue(self) -> float:
        # x > 500 : day
        # 500 > x > 250 : dim
        # 250 > x : dark
        x = self.getList()
        return float(x[4])

    def getHumidity(self) -> float:
        # Unit: %
        x = self.getList()
        return float(x[5])
        
    def getWindSpeed(self) -> float:
        # Unit: unknown, need complex math to get value
        x = self.getList()
        return float(x[6])
        
    def getPowerCheck(self) -> float:
        # 1: power is good, 0: power has failed (wait, if power failed how can it send this signal)
        x = self.getList()
        return float(x[7])

    def getPressure(self) -> float:
        # Unit: 10^x Pa
        x = self.getList()
        return float(x[8])