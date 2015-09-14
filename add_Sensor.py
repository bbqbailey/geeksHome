__author__ = 'superben'

Sensors = {}
zone=''
sensorName=''
sensorLoc=''
sensorType=''
sensorState=''
header=''
pin=''
gpio=''
direction=''

def check_for_exit( value):
    print("inside check_for_exit() function")
    print("value is: |" + value + "|")
    if(value == 'X' or value == 'x'):
        print("Found \'X\' or \'x\' so exiting")
        raise SystemExit
    print("Not exiting")
    return



print ("Adding Sensor - X to abort entry at any field, If Sensor State is set to Inactive, then remaining fields are set to \'\'")

zone = input("Zone: ")
check_for_exit(zone)

sensorName = input("Sensor Name: ")
check_for_exit(sensorName)

sensorLoc = input("Sensor Location: ")
check_for_exit(sensorLoc)


do_while=True
while do_while:
    sensorType = input("Sensor Type [MagneticSwitch,DeviceSwitch]: ")
    check_for_exit(sensorType)
    if(sensorType == 'MagneticSwitch' or sensorType == 'DeviceSwitch'):
        do_while = False
    else:
        print ("Check spelling: must be one of MagneticSwitch or DeviceSwitch")


do_while=True
while do_while:
    sensorState = input("Sensor State [Active, Inactive]: ")
    check_for_exit(sensorState)
    if(sensorState != 'Inactive' and sensorState != 'Active'):
        continue
    elif(sensorState == 'Inactive'):
        print("Sensor State is Inactive, so setting remainder to \'\' values")
        #they are initialized to this value at start of module
        do_while = False
    elif(sensorState == 'Active'):
        header = input("Beagle Header [P8,P9]: ")
        check_for_exit(header)

        pin = input("Beagle Header Pin [11, 12]: ")
        check_for_exit(pin)

        gpio = input("Beagle GPIO pin [44, 45]: ")
        check_for_exit(gpio)

        direction = input("Beagle Direction [in, out]: ")
        check_for_exit(direction)

        do_while = False

print("Finished defining sensor.")

Sensors[zone + '-' + sensorName] = {
        'Zone':zone, 'sensorName':sensorName, 'sensorLoc':sensorLoc, 'sensorType':sensorType,
        'sensorState':sensorState, 'header':header, 'pin':pin, 'direction':direction
}

print(Sensors)

for x in Sensors:
    if (x != 'Fields'):
        print(x, Sensors[x])
