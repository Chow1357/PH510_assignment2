#!/opt/software/anaconda/python-3.10.9/bin/python
"""
code tha

Tested using:
    Python 3.10.9
    mpi4py
"""
import numpy as np 
import math 

class Vector:
	def _init_(self, x, y, z) # initialise vector components
		self.x = x 
		self.y = y
		self.z = z 
	def _repr_(self):
		return f"Vector({self.x}, {self.y}, {self.z})

	def __add__(self, other):
		return Vector(self.x + other.x,
	
	def _magnitude_(self): 
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)


# using the object class 
#initialise vector with components
v1 = Vector(1, 2, 3) 

print(v1) # prints the vector v1 (1, 2, 3) 
print("Magnitude:", v1.magnitude()) # computes the magnitude of vector v1

 


