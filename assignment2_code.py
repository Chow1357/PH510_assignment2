#!/opt/software/anaconda/python-3.10.9/bin/python
"""
code tha

Tested using:
    Python 3.10.9
"""
#defining the required math functions for regular operations and for handling complex functions
import cmath 
import math 
# defining the new parent class called vector
class Vector:
	def __init__(self, x, y, z): # initialise vector components
		self.x = x 
		self.y = y
		self.z = z 
	# prints the vector in the form required
	def __repr__(self):
		return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"
	# defines the method for adding vectors 
	def __add__(self, other):
		return self.__class__(self.x + other.x,self.y + other.y, self.z + other.z) # adds two vectors and returns a resulting vector as an instance 
	#same method for addition but using sub instead
	def __sub__(self, other):
		return self.__class__(self.x - other.x,self.y - other.y, self.z - other.z)# subtracts two vectors
	# defining scalar multiplication 
	def __mul__(self, a):
		if isinstance(a, (int, float, complex)):
			return self.__class__(
				a * self.x,
				a * self.y, 
				a * self.z) 
		return NotImplemented
		
	def magnitude(self): 
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def scalar_product(self, other): 
		return (self.x*other.x + self.y*other.y + self.z*other.z)

	def cross_product(self, other): 
		return self.__class__(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z,
                self.x*other.y - self.y*other.x)  


# using the object class 
#initialise vector with components
v1 = Vector(1, 2, 3) 
v2 = Vector(4, 5, 6)

v3 = v1 + v2 
v4 = v2 - v1

print(v3)
print(v4)
#print(v3.x, v3.y, v3.z)
print(v1) # prints the vector v1 (1, 2, 3) 
print("cross product:", v1.cross_product(v2))
print("scalar product:", v1.scalar_product(v2))
print("Magnitude:", v1.magnitude()) # computes the magnitude of vector v1

#-----------Task 2--------------------
#instantiate the vectors which represent the cartesian points for each triangle
# Triangle 1 
A1 = Vector(0,0,0) 
B1 = Vector(1,0,0) 
C1 = Vector(0,1,0)
#Triangle 2 
A2 = Vector(-1,-1,-1)
B2 = Vector(0,-1,-1)
C2 = Vector(-1,0,-1) 
#Triangle 3
A3 = Vector(1,0,0)
B3 = Vector(0,0,1)
C3 = Vector(0,0,0)
#Triangle 4 
A4 = Vector(0,0,0)
B4 = Vector(1,-1,0)
C4 = Vector(0,0,1)

#defining the function to find the area of the triangles 
def triangle_area(A, B, C):
   AB = B - A 
   AC = C - A 
   return 0.5 * AB.cross_product(AC).magnitude()

#print the area of the four seperate triangles 
print("Triangle 1 area:", triangle_area(A1, B1, C1)
print("Triangle 2 area:", triangle_area(A2, B2, C2)
print("Triangle 3 area:", triangle_area(A3, B3, C3)
print("Triangle 4 area:", triangle_area(A4, B4, C4)

#-----part B--------
#define the function to calculate the internal angles of the triangles
def angle_between(u, v):
    dot = u.scalar_product(v)
    mag_u = u.magnitude()
    mag_v = v.magnitude()
    return math.acos( dot / (mag_u * mag_v) )
# function that fidns the edges of the triangle between which the internal angles are 
def triangle_angles(A, B, C): 
    AB = B-A
    AC = C-A 

    BA = A-B
    BC = C-B 

    CA = A-C
    CB = B-C 
    
    angle_A = angle_between(AB, AC) 
    angle_B = angle_between(BA, BC)
    angle_C = angle_between(CA, CB)
    return angle_A, angle_B, angle_C
#defining the four triangles with the cartesian vectors I instantiated after the vector class 
triangles = [("triangle_1", A1, B1, C2),
    ("triangle_2", A2, B2, C2),
    ("triangle_3", A3, B3, C3),
    ("triangle_4", A4, B4, B4)]
# a for loop which goes through the four triangles and prints the internal angles using the edges we have defined
for name, A, B, C in triangles:
    angles = trangle_angles(A, B, C)
    angles_deg = [math.degress(a) for a in angles]
    print(f"{name} angles (degrees): {angles_deg}")


