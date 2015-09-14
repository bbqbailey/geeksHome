__author__ = 'superben'
#Zone, SensorName, SensorLocation,          SensorType,     SensorState, Header, Pin, GPIO, Direction

Sensors={}
print("Opening file sensors.txt")

f=open('sensors.txt','r')

firstTime=True

for line in f:
    #print(line)

    lineSplit=line.split(',')
    #print("Split:  " + str(lineSplit))

    lineStripped=[x.strip(' ') for x in lineSplit]
    #print("Stripped: " + str(lineStripped))

    if(firstTime == True):
        Sensors['Fields'] = lineStripped
        firstTime=False
    else:
        zone=lineStripped[0]
        sensorName=lineStripped[1]
        Sensors[zone + '-' + sensorName] = lineStripped

print(Sensors)

for x in Sensors:
    if (x != 'Fields'):
        print(x, Sensors[x])

