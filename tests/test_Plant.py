""" 
    Tests the file Plant.py
    Focuses on
        -objects having the right type
        -functions returning the correct value
        -functions setting the correct value
"""
from src.Plant import Plant
import datetime


def test_types():
    testing = Plant()
    testing.setName("")
    testing.setLast_watered(datetime.datetime.now())
    testing.setWatering_interval(datetime.timedelta(0))
    testing.setWatering_time(datetime.datetime.now().time())
    assert type(testing.getName()) is str
    assert type(testing.getLast_watered()) is datetime.datetime
    assert type(testing.getWatering_interval()) is datetime.timedelta
    assert type(testing.getWatering_time()) is datetime.time


def test_getting():
    parameters = (datetime.timedelta(2),datetime.datetime.now())
    testing = Plant(parameters[0],parameters[1])
    assert testing.getWatering_interval() == parameters[0]
    assert testing.getLast_watered() == parameters[1]

    watering_time = testing.setWatering_time(datetime.time(3))
    testing.setWatering_time(watering_time)
    assert testing.getWatering_time() == watering_time

    testName = "test"
    testing.setName(testName)
    assert testing.getName() == testName

def test_setting():
    testing = Plant()

    #setting name
    name = "new_name"
    testing.setName(name)
    assert testing.getName() == name

    #setting interval
    interval = datetime.timedelta(3,23,2020)
    testing.setWatering_interval(interval)
    assert testing.getWatering_interval() == interval

    #setting time
    time = datetime.time(1,2,3,4)
    testing.setWatering_time(time)
    assert testing.getWatering_time() == time

    #setting last watered
    watering = datetime.date(5,6,7)
    testing.setLast_watered(watering)
    assert testing.getLast_watered() == watering