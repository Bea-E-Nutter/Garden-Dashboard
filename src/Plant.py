import datetime

class Plant:
    #Gets an obj's attributes
    def getName(self) -> str:
        return self.__name
    def getWatering_interval(self) -> datetime.timedelta:
        return self.__watering_interval
    def getWatering_time(self) -> datetime.time:
        return self.__watering_time
    def getLast_watered(self) -> datetime.datetime:
        return self.__last_watered

    #Sets an obj's attributes
    def setName(self,new_name):
        self.__name = new_name
    def setWatering_interval(self,new_date):
        self.__watering_interval = new_date
    def setWatering_time(self,new_time):
        self.__watering_time = new_time
    def setLast_watered(self,new_watering):
        self.__last_watered = new_watering

    #When obj is initialized, this sets a name, period between watering, what time the plant is watered, and when the plant was last watered
    def __init__(self,plant_watering_interval = datetime.timedelta(1), plant_watering_time = datetime.datetime.now().time(), plant_last_watered = datetime.datetime.now()):
        self.setWatering_interval(plant_watering_interval)
        self.setWatering_time(plant_watering_time)
        self.setLast_watered(plant_last_watered)