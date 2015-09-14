__author__ = 'superben'

#load the sensor pickle file

import pickle


Sensors = pickle.load( open( "Sensors.p", "rb"))

for x in Sensors.keys():
    print(x)
    print(Sensors[x])


