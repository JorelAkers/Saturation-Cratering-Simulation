#!/usr/bin/env python
#Authors: Jorel Akers, Alison Frideli
#ASTR 3750, Planets, Moons and rings
#Impact crater saturation simulation
#Almost all functions used in this programs are stored in crater_functions.py
from crater_functions import *

#same object but with more fields to compensate for additional complexity of the drater diameter formula.
class Impactor(object):
	def __init__(self, x=None, y=None, Idiameter= None, Cdiameter= None, Iradius = None, Cradius = None,Carea = None,age = None, angle = None,density= None, mass = None, velocity = None):
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
		#density of impactor
		self.density = density
		#mass of impactor
		self.mass = mass
		#Velocity of impactor at time of impact.
		self.velocity = velocity
		
# new object to describe the planet or moon we are modeling. Adding this class allows us to model the impacts on any planet we want.
class Planet(object):
	def __init__(self, name = None, density = None, radius = None, mass = None, gravity = None, EscapeV = None):
		self.name = name
		self.density = density
		self.radius = radius
		self.mass = mass
		self.gravity = gravity
		self.EscapeV = EscapeV
# constructor for the planet.
def new_planet(array, rho, rad, name):
	#defining the gravitational constant for use in determining surface gravity and escape velocity (Units: km^3 per kg s^2)
	G = 6.6742*(10**(-20))
	#average density of the planet (Units: kg per km^3
	density = rho
	#radius of planet (mean distance from core to surface) (Units: km)
	radius  = rad
	#volume of planet dervied from radius (Units: km^3)
	volume = (4.0/3)*(math.pi)*radius**3
	#mass of planet derived from density and volume (Units: kg)
	mass = volume*density
	#strength of gravity field at the surface. determined by planet mass and radius (Units: km per s^2)
	gravity = (G*mass)/(radius**2)
	#escape velocity of the planet. (Units: km/s)
	EscapeV = ((2.0*G*mass)/(radius))**(0.5)
	array.append(Planet(name, density, radius, mass, gravity, EscapeV))

#This constructor differs from part one in a few respects.  We will be using a more complicated formula to determine the crater diameter.  To use this formula we require several new features
def new_impactor2(Array,den, loop, planet):
	#define a random value for the x,y coordinates of the epicenter of the crater.  Pulled from a uniform distribution.
	x = np.random.uniform(1,500)
	y = np.random.uniform(1,500)
	#This section is used to vary the size of the impactors. We decided to consider craters between 10-100 Km in diameter and broke
	#down the distribuiton to the following: 10% 1-2 Km, 80% 3-8 Km , 10% 9-10 Km 
	det = np.random.random_sample()
	if det < 0.1:
		Idiameter = np.random.uniform(1,2)
	if det > 0.9:
		Idiameter = np.random.uniform(9,10)
	else:
		Idiameter = np.random.uniform(3,8)
	#Idensity is the density of the impactor
	Idensity = den
	#Iradius the radius of the impactor
	Iradius = (Idiameter)/2
	#mass of the impactor using density multiplied by volume.
	Imass = Idensity * ((4/3)*(math.pi)*(Iradius**3))
	#defining the velocity of the impactor at the escape velocity of the planet.
	Ivelocity = planet.EscapeV
	#the kinetic energy of the impactor
	IEnergy = (0.5)*(Imass)*(Ivelocity)**2
	#the angle of impact in radians.  We constricted the angle between +- pi/4 to keep circular craters.
	Iangle = math.radians(np.random.uniform(-45,45))
	#using the complex relation found on Slide 16 of the lecture notes to determine the diameter of the crater.
	Cdiameter = (((2*Idensity**(0.11))*(Iradius**(0.12))*(IEnergy**(0.22))*((math.sin(Iangle))**(1/3))/(((planet.density)**0.33)*((planet.gravity)**0.22))))
	#crater radius derived from diameter
	Cradius = (Cdiameter)/2
	#area of the crater
	Carea = (math.pi)*(Cradius)**2
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
	Array.append(Impactor(x,y,Idiameter,Cdiameter, Iradius, Cradius, Carea, age, Iangle, Idensity, Imass, Ivelocity))

def main():
	rockrho = 3.334*(10**12) #average density of rock in kg/km^3
	loopcount = 0
	#the craters list is the container for all our impactor objects.
	craters = []
	#the time list is the container for the time axis in our num of craters v time plot
	time = []
	#container for number of craters at a given time.
	numcraters = []
	planet = []
	#let's pick a planet.  How about the moon!
	moonrho = 3.334*(10**12) #kg/Km^3
	moonrad = 1737.1 #Km
	new_planet(planet, moonrho, moonrad, 'Moon')
	#calls the loop2 function from crater_functions.py
	loop2(loopcount, craters, time, numcraters, rockrho, planet)
	

if __name__ == '__main__':
	main()
