#Code for Plotting Dissipation of Heat from LN2 filled bowl surrounded by foam vs not surrounded by foam
#Anna Kofman
#April 10th, 2017

import numpy as np
import matplotlib.pyplot as plt


time_nofoam_secs = []
time_nofoam_mins = []
temp_nofoam = []

time_foam_secs = []
time_foam_mins = []
temp_foam = []

for line in open('/Users/Anna/Documents/Vieira_Research/Code/FoamCoolerPlot/3.txt', 'r'):
    line = line.split()
    time_nofoam_secs.append(float(line[0]))
    temp_nofoam.append(float(line[1]))

for line in open('/Users/Anna/Documents/Vieira_Research/Code/FoamCoolerPlot/4.txt', 'r'):
    line = line.split()
    time_foam_secs.append(float(line[0]))
    temp_foam.append(float(line[1]))

for a in time_nofoam_secs:
    time_nofoam_mins.append(a/60)
for a in time_foam_secs:
    time_foam_mins.append(a/60)
    
#create the fig and ax objects
fig, ax = plt.subplots()

#ax.plot(time_nofoam_mins,temp_nofoam, lw = 2, label = "Stainless Steel Bowl (No foam)")
#ax.plot(time_foam_mins,temp_foam, lw = 2, label = "Stainless Steel Bowl (Surrounded by foam)")


ax.semilogy(time_nofoam_mins,temp_nofoam, lw = 2, label = "Stainless Steel Bowl (No foam)")
ax.semilogy(time_foam_mins,temp_foam, lw = 2, label = "Stainless Steel Bowl (Surrounded by foam)")
#ax.loglog(time_nofoam_mins,temp_nofoam, lw = 2, basex=np.e,basey=np.e, label = "Stainless Steel Bowl (No foam)")
#ax.loglog(time_foam_mins,temp_foam, lw = 2, basex=np.e,basey=np.e, label = "Stainless Steel Bowl (Surrounded by foam)")
plt.title('LN2 Cold Chamber Test')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (K)')
plt.legend(loc='best')
plt.show()





