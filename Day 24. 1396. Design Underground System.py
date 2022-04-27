#Day 24.
#1396. Design Underground System

from statistics import mean
class UndergroundSystem:

    def __init__(self):
        self.checkedIn = dict()
        self.avg = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedIn:
            self.checkedIn[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkedIn:
            boarding,bt = self.checkedIn.pop(id)
        if (boarding,stationName) not in self.avg:
            self.avg[(boarding,stationName)] = [t - bt]
        else:
            self.avg[(boarding,stationName)].append((t - bt))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation,endStation) in self.avg:
            return mean(self.avg[(startStation,endStation)])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
