import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import csv
from array import *
from projectpart1 import new_impactor
from projectpart2 import new_impactor2
#This function takes all of the craters and compares them to each other. deleteing all of the older craters with new craters covering
#thier epicenters.
def update_craters(Craters):
	#a is an index used to delete the craters.  without it you occasionally end up with an index out of bounds of the list.
	a = 0
	#cycle through each crater in the list
	for crater in Craters:
		#cycle each other crater in the list
		for other in Craters:
			#just in case it tries to compar a crater with itself.
			if crater is other:
				continue
			#compute the distance between the epicenters
			dx = (other.x-crater.x)
			dy = (other.y-crater.y)
			dist = math.sqrt(dx**2.0 + dy**2.0)
			#if the epicenter of the current crater falls within the radius of another and the age of the other crater is younger 
			#(younger in this case is a larger number) then delete the current crater
			if dist < other.Cradius and other.age > crater.age:
				#just in case the current crater is the most recent
				if a == len(Craters):
					#set the index a to the actual index of the crater.
					a = (len(Craters)-1)
				#delete the crater!
				del Craters[a]
		#increment the index
		a += 1
#This function builds the scatter plots that represent our simulated area
def draw_craters(craters, ind):
	#set the boundaries of the are to 500 by 500 Km
	plt.axis([0,500,0,500])
	#for each crater plot a circle
	for crater in craters:
			#plot the circle
			plt.scatter(crater.x,crater.y, s=crater.Carea, c='b', alpha = 0.5)
	#axes labels and title for plot
	#print ind
	#sys.exit()
	ptime = 'Craters at year {0}'.format(ind*1000)
	plt.title(ptime)
	plt.xlabel('Distance (Km)')
	plt.ylabel('Distance (Km)')
	#plt.legend()
	#set the label name for our picture output
	index = 'snap{0}.png'.format(ind)
	#save a picture of the simulated field.
	plt.savefig(index, bbox_inches='tight')
	#clear the scatter plot
	plt.cla()
	#txt_out(ind, craters)
	
#This function draws out Number of craters vs time plot.
def draw_timeplot(Timeaxis, Crataxis, index):
		#draw the plot from the data in the two lists.
		plt.plot(Timeaxis, Crataxis)
		#labels and title
		plt.title('Number of Craters vs. Time')
		plt.xlabel('Time (e+03 years)')
		plt.ylabel('# of Craters')
		#save a picture
		ind = 'timeplot{0}.png'.format(index/100)
		plt.savefig(ind, bbox_inches='tight')
		#display the plot.
		plt.show()
		plt.cla()
#outputs a text file with each plot.
def txt_out(Time, Craters, ind):
	index = 'Ncratersandtime{0}.txt'.format(ind)
	print 'index is: {0}, time is: {1}, Numcraters is : {2}'.format(ind, Time[ind-1], Craters[ind-1])
	np.savetxt(index, (Time[ind-1], Craters[ind-1]), header = 'Format is:\n Time\n Number of Craters')
#outputs a csv file with the time and number of craters data from the simulation.
def csv_out(Time, Craters):
	np.savetxt('timeplotdata.csv',(Time, Craters), delimiter = ',')

#Where the bulk of other functions are called. Also handles building the time and crater number data sets.
def loop(loopcount, crarr, Taxis, CNUMaxis):
	#run until we hit the magic sys.exit() statment
	while True:
		#make a new impactor
		new_impactor(crarr, loopcount)
		#update and possibly delete craters
		update_craters(crarr)
		#increment the loop count
		loopcount += 1
		#early snapshot at 10000 years
		if (loopcount == 10):
			draw_craters(crarr, loopcount)
		#this statement will take a snapshot every 100000 years	
		if (loopcount % 100) == 0:
			draw_craters(crarr, loopcount)
		#add the current loopcount (millenium) to the time axis data
		Taxis.append(loopcount)
		#add the current number of craters to the number of craters data
		CNUMaxis.append(len(crarr))
		#output Time and crater number data for every snapshot
		if loopcount == 10 or loopcount % 100 ==0:
			txt_out(Taxis, CNUMaxis, loopcount)
		#at one million years output data as a csv, take a final snapshot and plot Time versus Number of craters
		#then exit program.
		if (loopcount) == 1000:
			csv_out(Taxis, CNUMaxis)
			draw_craters(crarr, loopcount)
			draw_timeplot(Taxis, CNUMaxis, loopcount)
			txt_out(Taxis, CNUMaxis, loopcount)
			sys.exit()
	
def loop2(loopcount, crarr, Taxis, CNUMaxis, den, planet):
	#run until we hit the magic sys.exit() statment
	while True:
		#make a new impactor
		new_impactor2(crarr, den, loopcount, planet[0])
		#update and possibly delete craters
		update_craters(crarr)
		#increment the loop count
		loopcount += 1
		#early snapshot at 10000 years
		if (loopcount == 10):
			draw_craters(crarr, loopcount)
		#this statement will take a snapshot every 250000 years.	
		if (loopcount % 250) == 0:
			draw_craters(crarr, loopcount)
		#add the current loopcount (millenium) to the time axis data
		Taxis.append(loopcount)
		#add the current number of craters to the number of craters data
		CNUMaxis.append(len(crarr))
		print 'year: {0}'.format(loopcount*1000)
		#output Time and crater number data for every snapshot
		if loopcount == 10 or loopcount % 250 ==0:
			txt_out(Taxis, CNUMaxis, loopcount)
		#at 1.5 million years output data as a csv, take a final snapshot and plot Time versus Number of craters
		#then exit program.
		if loopcount == 1600:
			csv_out(Taxis, CNUMaxis)
			draw_craters(crarr, loopcount)
			draw_timeplot(Taxis, CNUMaxis, loopcount)
			txt_out(Taxis, CNUMaxis, loopcount)
			sys.exit()
