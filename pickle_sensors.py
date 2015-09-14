__author__ = 'superben'

#Save sensor dictionary to pickled file
#
#This builds the original pickle file.  It's combersome so create ability to add sensors later
#

import pickle

Sensors={}

sensor=['Zone','SensorName','SensorLocation','SensorType','SensorState','Header','Pin','GPIO','Direction']
zone=sensor[0]
sensorName=sensor[1]
sensorLoc=sensor[2]
sensorType=sensor[3]
sensorState=sensor[4]
header=sensor[5]
pin=sensor[6]
gpio=sensor[7]
direction=sensor[8]

Sensors['Fields'] = {
        'Zone':zone, 'sensorName':sensorName, 'sensorLoc':sensorLoc, 'sensorType':sensorType,
        'sensorState':sensorState, 'header':header, 'pin':pin, 'direction':direction
}


sensor=['Porch', 'ScreenDoor', 'ScreenDoor interior frame', 'MagneticSwitch', 'Active', 'P8', '11', '44', 'in']
zone=sensor[0]
sensorName=sensor[1]
sensorLoc=sensor[2]
sensorType=sensor[3]
sensorState=sensor[4]
header=sensor[5]
pin=sensor[6]
gpio=sensor[7]
direction=sensor[8]

Sensors[zone + '-' + sensorName] = {
        'Zone':zone, 'sensorName':sensorName, 'sensorLoc':sensorLoc, 'sensorType':sensorType,
        'sensorState':sensorState, 'header':header, 'pin':pin, 'direction':direction
}


sensor=['Porch', 'HouseDoor',  'Inside house, on door frame', 'MagneticSwitch', 'Inactive', '', '', '', '']
zone=sensor[0]
sensorName=sensor[1]
sensorLoc=sensor[2]
sensorType=sensor[3]
sensorState=sensor[4]
header=sensor[5]
pin=sensor[6]
gpio=sensor[7]
direction=sensor[8]

Sensors[zone + '-' + sensorName] = {
        'Zone':zone, 'sensorName':sensorName, 'sensorLoc':sensorLoc, 'sensorType':sensorType,
        'sensorState':sensorState, 'header':header, 'pin':pin, 'direction':direction
}


sensor=['Porch', 'PIR', 'On porch, above house door', 'DeviceSwitch', 'Inactive', '', '', '', '']
zone=sensor[0]
sensorName=sensor[1]
sensorLoc=sensor[2]
sensorType=sensor[3]
sensorState=sensor[4]
header=sensor[5]
pin=sensor[6]
gpio=sensor[7]
direction=sensor[8]

Sensors[zone + '-' + sensorName] = {
        'Zone':zone, 'sensorName':sensorName, 'sensorLoc':sensorLoc, 'sensorType':sensorType,
        'sensorState':sensorState, 'header':header, 'pin':pin, 'direction':direction
}

sensor=['Porch', 'Fire', 'On porch, at apex above kitchen window', 'DeviceSwitch', 'Inactive', '', '', '', '']
zone=sensor[0]
sensorName=sensor[1]
sensorLoc=sensor[2]
sensorType=sensor[3]
sensorState=sensor[4]
header=sensor[5]
pin=sensor[6]
gpio=sensor[7]
direction=sensor[8]

Sensors[zone + '-' + sensorName] = {
        'Zone':zone, 'sensorName':sensorName, 'sensorLoc':sensorLoc, 'sensorType':sensorType,
        'sensorState':sensorState, 'header':header, 'pin':pin, 'direction':direction
}

pickle.dump ( Sensors, open("Sensors.p","wb"))

"""
for x in Sensors.keys():
    print(x)
    print(Sensors[x])
"""
