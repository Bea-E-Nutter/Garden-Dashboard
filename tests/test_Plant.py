""" 
    Tests the file Plant.py
    Focuses on
        -objects having the right type
        -functions returning the correct value
        -functions setting the correct value
"""
import src.Plant as p
import datetime


def test_types():
    testing = p.Plant()
    assert type(testing.getName()) is str
    assert type(testing.getLast_watered()) is datetime.datetime
    assert type(testing.getWatering_interval()) is datetime.timedelta
    assert type(testing.getWatering_time()) is datetime.time


def test_getting():
    parameters = ("name",datetime.timedelta(2), datetime.datetime.now().time(),datetime.datetime.now())
    testing = p.Plant(parameters[0],parameters[1],parameters[2],parameters[3])
    assert testing.getName() == parameters[0]
    assert testing.getWatering_interval() == parameters[1]
    assert testing.getWatering_time() == parameters[2]
    assert testing.getLast_watered() == parameters[3]

def test_setting():
    testing = p.Plant()

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