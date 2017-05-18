#Code for plotting thermocouple readout vs. time for two thermocouples
#Anna Kofman
#May 17, 2017

import numpy as np
import matplotlib.pyplot as plt

###*******  ENTER ALL NECESSARY DATA HERE  *********###
disk_path = #ENTER PATH TO DISK DATA HERE
stand_path = #ENTER PATH TO STAND DATA HERE
plot_title = #ENTER THE TITLE OF THE PLOT YOU WANT TO CREATE
x_label = #ENTER X-AXIS LABEL
y_Label = #ENTER Y_AXIS LABEL
type_of_stand = #ENTER MATERIAL STAND IS MADE FROM


#initiate necessary arrays
disk_time_secs = []
disk_time_mins = []
disk_temp = []

stand_time_secs = []
stand_time_mins = []
stand_temp = []

#iterates through lines in disk file
for line in open(disk_path, 'r'):
    #splits the lines on spaces
    line = line.split()
    #appends the time value from each line to the corresponding time array
    disk_time_secs.append(float(line[0]))
    #appends the temp value from each line to the corresponding temp array
    disk_temp.append(float(line[1]))
    
#iterates through lines in stand file
for line in open(stand_path, 'r'):
    #splits the lines on spaces
    line = line.split()
    #appends the time value from each line to the corresponding time array
    stand_time_secs.append(float(line[0]))
    #appends the temp value from each line to the corresponding temp array
    stand_temp.append(float(line[1]))

#converts time to minutes
for a in disk_time_secs:
    disk_time_mins.append(a/60)

#converts time to minutes
for a in stand_time_secs:
    stand_time_mins.append(a/60)


#create the fig and ax objects
fig, ax = plt.subplots()

#plots the disk data and then the stand data
ax.plot(disk_time_mins,disk_temp, lw = 2, label = "Disk")
stand = type_of_stand + " Stand"
ax.plot(stand_time_mins,stand_temp, lw = 2, label = stand)

#adding all the necessary plot information
ax.minorticks_on()
plt.title(plot_title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend(loc = 'best')
plt.show()

