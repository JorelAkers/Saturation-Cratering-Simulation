#!/usr/bin/env python
#Authors: Jorel Akers, Alison Frideli
#ASTR 3750, Planets, Moons and rings
#Impact crater saturation simulation
#Almost all functions used in this programs are stored in crater_functions.py
from crater_functions import *

#First we must define the impactor object and it's parameters.  This will be used in part two as well.
class Impactor(object):
	def __init__(self, x=None, y=None, Idiameter= None, Cdiameter= None, Iradius = None, Cradius = None,Carea = None,age = None, angle = None, mass = None, velocity = None):
		self.x = x
		self.y = y
		#diameter of the Impactor
		self.Idiameter = Idiameter
		#diameter of the Crater
		self.Cdiameter = Cdiameter
		#radius of the Impactor
		self.Iradius = Iradius
		#radius of the Crater
		self.Cradius = Cradius
		#total area of the Crater
		self.Carea = Carea
		#time of impact in thousands of years.
		self.age = age
		#angle of impact with respect to ground.
		self.angle = angle
		#mass of impactor
		self.mass = mass
		#Velocity of impactor at time of impact.
		self.velocity = velocity
		#angle, mass and velocity are neglected for part 1.
		
#now we define the constructor for each impactor with values relevant for part 1. Impactors are stored in a list (Array) and the age parameter depends on the loop number.
def new_impactor(Array, loop):
	#define a random value for the x,y coordinates of the epicenter of the crater.  Pulled from a uniform distribution.
	x = np.random.uniform(1,500)
	y = np.random.uniform(1,500)
	#This section is used to vary the size of the impactors. We decided to consider craters between 10-50 KM 99% of the time and only introduce
	#craters varying from  50 Km to 100 KM 1% of the impacts
	det = np.random.random_sample()
	if det < 0.1:
		Idiameter = np.random.uniform(1,2)
	if det > 0.9:
		Idiameter = np.random.uniform(9,10)
	else:
		Idiameter = np.random.uniform(3,8)
	#the following four attributes are derived from Idiameter
	Cdiameter = Idiameter*10.0
	Iradius = (Idiameter)/2.0
	Cradius = Cdiameter/2.0
	Carea = (math.pi)*(Cradius)**2.0
	#age of impact is the loop number times 1000 years.
	age = loop*1000
	#The following if statements bound the impacts to within the area limits. We've noticed that from output pictues they seem to extend past
	#the limit on the y axis, but on inspection of the scatter plot by expanding the image this is just a quirk of matplotlib.
	if (x + Cradius) > 500:
		x = 500 - Cradius
	if (x - Cradius) < 0:
		x = 0 + Cradius 
	if (y + Cradius) > 500:
		y = 500 - Cradius
	if (y - Cradius) < 0:
		y = 0 + Cradius 
	#and finally we add the impactor object into our craters list.
	Array.append(Impactor(x,y,Idiameter,Cdiameter, Iradius, Cradius,Carea, age, 0, 0, 0))
#the main function sets the simulation into motion.	
def main():
	#loopcount is our time counter
	loopcount = 0
	#the craters list is the container for all our impactor objects.
	craters = []
	#the time list is the container for the time axis in our num of craters v time plot
	time = []
	#container for number of craters at a given time.
	numcraters = []
	#calls the loop function from crater_functions.py
	loop(loopcount, craters, time, numcraters)
	

if __name__ == '__main__':
	main()
