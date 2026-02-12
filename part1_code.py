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
	def __init__(self, x, y, z): # initialise vector components
		self.x = x 
		self.y = y
		self.z = z 
	def __repr__(self):
		return f"Vector({self.x}, {self.y}, {self.z})"

	def __add__(self, other):
		return Vector(self.x + other.x,self.y + other.y, self.z + other.z) # adds two vectors and returns a resulting vector as an instance 
	
	def __sub__(self, other):
		return Vector(self.x - other.x,self.y - other.y, self.z - other.z)# subtracts two vectors
	
	def magnitude(self): 
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)


# using the object class 
#initialise vector with components
v1 = Vector(1, 2, 3) 
v2 = Vector(4, 5, 6)

v3 = v1 + v2 

print(v1 + v2)
print(v3.x, v3.y, v3.z)
print(v1) # prints the vector v1 (1, 2, 3) 
print("Magnitude:", v1.magnitude()) # computes the magnitude of vector v1

 


