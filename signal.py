#Import Libraries
#
import sys
import numpy as np
import struct

#Declaring variables and assigning them values
#
sample_rate = 8000
freq = 100
samples = 64000
x = np.arange(samples)

#Equation to create the sine wave
#
y = 10000*np.sin(2*np.pi*freq*x/sample_rate)

#Writing data to a binary file
#
f = open(sys.argv[1],'wb')

#Getting all the sine wave data with a for loop
#
for i in y:

    #Writing 4 bytes per sample
    #
    f.write(struct.pack('f', samples))

    #Closing file
    #
f.close()
