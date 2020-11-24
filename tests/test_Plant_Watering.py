from src.Plant import Plant
import datetime

def test_Need_Watering():
    testing = Plant(datetime.timedelta(7), datetime.datetime(2020,3,29)) #Date that it should be watered is 4/5/2020

    #Before 4/5 should not need water
    assert testing.needsWatering(datetime.datetime(2020,3,30)) == False
    assert testing.needsWatering(datetime.datetime(2020,4,1)) == False
    assert testing.needsWatering(datetime.datetime(2020,4,4,23,59,59)) == False

    #4/5 or after should need water
    assert testing.needsWatering(datetime.datetime(2020,4,5)) == True
    assert testing.needsWatering(datetime.datetime(2021,3,29)) == True

def test_Time_Til_Watering():
    testing = Plant(datetime.timedelta(7), datetime.datetime(2020,3,29))

    #4/5/2020 is when plant should be watered
    assert testing.timeTilWatering(datetime.datetime(2020,4,5)).total_seconds() == 0

    #86400 seconds in a day
    assert testing.timeTilWatering(datetime.datetime(2020,4,4)).total_seconds() == 86400
    assert testing.timeTilWatering(datetime.datetime(2020,4,4,12)).total_seconds() == 43200
    assert testing.timeTilWatering(datetime.datetime(2020,4,4,23,59,59)).total_seconds() == 1

    #returns negative when the time given is after when watering is due
    assert testing.timeTilWatering(datetime.datetime(2020,4,6)).total_seconds() == -86400
    assert testing.timeTilWatering(datetime.datetime(2020,4,5,0,0,1)).total_seconds() == -1