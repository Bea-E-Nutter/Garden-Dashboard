import datetime

class Plant:

    #When obj is initialized a period between watering and when the plant was last watered
    def __init__(self,plant_watering_interval = datetime.timedelta(1), plant_last_watered = datetime.datetime.now()):
        self._name = ""
        self._last_watered = plant_last_watered
        self._watering_time = datetime.time(0)
        self._watering_interval = plant_watering_interval

    @property
    def last_watered(self) -> datetime.datetime:
        return self._last_watered
    @last_watered.setter
    def last_watered(self, new_watering:datetime.datetime):
        self._last_watered = new_watering

    @property
    def watering_time(self) -> datetime.time:
        return self._watering_time
    @watering_time.setter
    def watering_time(self, new_time:datetime.time):
        self._watering_time = new_time

    @property
    def watering_interval(self) -> datetime.timedelta:
        return self._watering_interval
    @watering_interval.setter
    def watering_interval(self, new_interval:datetime.timedelta):
        self._watering_interval = new_interval
    
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, new_name:str):
        self._name = new_name

    #Returns true if the plant needs water
    def needsWatering(self, date:datetime.datetime = datetime.datetime.now()) -> bool:
        return self.timeTilWatering(date).total_seconds() <= 0

    #Returns a time delta obj that contains the amount of time until the plant needs water
    def timeTilWatering(self, date: datetime.datetime) -> datetime.timedelta:
        return (self.last_watered + self.watering_interval)-date
