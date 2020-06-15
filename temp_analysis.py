import pyfirmata
import time
from pyfirmata import Arduino, util
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *



#Used pyFirmata to interface python with arduino
 #**https://github.com/tino/pyFirmata
 #**https://realpython.com/arduino-python/
#Uploaded StandardFirmata Arduino  
#Used Mathlab library to plot data
 #**https://realpython.com/python-matplotlib-guide/

#TODO:Add Buzzer 

#Function to make the Plot Graph
def make_graph():
  plt.ylim(0,100)
  plt.xlim(0,15)
  plt.title('Live Temperature Data')
  plt.grid(True)
  plt.ylabel('Temperature')
  plt.plot(tempA,'-ro',color='blue',label='Degrees F')
  plt.legend(loc='upper left')

counter=0
tempA=[]

#Setting up the board path
board= pyfirmata.Arduino('/dev/cu.usbmodemFA131')
#Interactive mode on
plt.ion()

#Initializing board
it=pyfirmata.util.Iterator(board)
it.start()

#Initializing temperature sensor
temp_sensor=board.get_pin('a:0:i')

#Initialing LED lights
led1=board.get_pin('d:13:o')
led2=board.get_pin('d:12:o')
led3=board.get_pin('d:11:o')


try:

 while True:
  voltage=temp_sensor.read()
   
  if voltage is not None:
    #Converting Voltage 
    temp=5.0*100*voltage
    #converting temperature to Fahrenheit
    temp1=(temp*1.8000)+32.00
    
    print ("{0} Fahrenheit".format(temp1))
    
    time.sleep(0.5)
   #Counter to resest the live graph
    counter=counter+1
   #Store sensor reading to array 
    tempA.append(temp1)
   #Cold:0-59(Blue Led ON), Warm:59-79(Green LED ON), Hot:79-100+(Red LED ON)  
    if temp1<=59:
      led3.write(1)
    elif temp1>59 and temp1<=79:
      led2.write(1)
    else: 
      led1.write(1)
    
   #Reset the graph to shown 15 data points on x-axis on the graph     
    if counter>16:
      tempA=[]
      counter=0
   #Create the graph with sensor data
    drawnow(make_graph)
    plt.pause(0.0001)
      
    time.sleep(0.1)
#Reset lights when stopped [ctrl z] 
except:
 led1.write(0)
 led2.write(0)
 led3.write(0)    
