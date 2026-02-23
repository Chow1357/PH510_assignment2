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
<<<<<<< HEAD
    def __init__(self, x, y, z): # initialise vector components
        self.x = x
        self.y = y
        self.z = z 
    # prints the vector in the form required
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"
    # defines the method for adding vectors 
    def __add__(self, other):
=======
	def __init__(self, x, y, z): # initialise vector components
		self.x = x
		self.y = y
		self.z = z
	# prints the vector in the form required
	def __repr__(self):
		return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"
	# defines the method for adding vectors 
	def __add__(self, other):
>>>>>>> 7743877930a6dd6a172ceeea7102ef16e4d6f13f
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
	# ensures that python can do both 2 * v as well as v * 2 
	__rmul__ = __mul__
	
	def magnitude(self): 
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def scalar_product(self, other): 
		return (self.x*other.x + self.y*other.y + self.z*other.z)

	def cross_product(self, other): 
		return self.__class__(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z,
                self.x*other.y - self.y*other.x)  


# using the object class 
#creating the vector objects
v1 = Vector(1, 2, 3) 
v2 = Vector(4, 5, 6)

#testing the add and subtract methods inside the parent class and returning two new vector objects v3 and v4 
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
print("Triangle 1 area:", triangle_area(A1, B1, C1))
print("Triangle 2 area:", triangle_area(A2, B2, C2))
print("Triangle 3 area:", triangle_area(A3, B3, C3))
print("Triangle 4 area:", triangle_area(A4, B4, C4))

#-----part B--------
#define the function to calculate the internal angles of the triangles
def angle_between(u, v):
    dot = u.scalar_product(v)
    mag_u = u.magnitude()
    mag_v = v.magnitude()
    return math.acos( dot / (mag_u * mag_v) )
# function that fidns the edges of the triangle between which the internal angles are 
def triangle_angles(A, B, C):
	# finding the vectors that meet at the vertex or cartesian point A 
    AB = B-A
    AC = C-A 
    # same method for vertex A 
    BA = A-B
    BC = C-B 

    CA = A-C
    CB = B-C 
    # calculating the angle between the defined vectors using the angle between function we defined
    angle_A = angle_between(AB, AC) 
    angle_B = angle_between(BA, BC)
    angle_C = angle_between(CA, CB)
    return angle_A, angle_B, angle_C
#storing the triangles  
triangles = [("triangle_1", A1, B1, C1),
    ("triangle_2", A2, B2, C2),
    ("triangle_3", A3, B3, C3),
    ("triangle_4", A4, B4, C4)]
# a for loop which goes through the four triangles and prints the internal angles using the edges we have defined
for name, A, B, C in triangles:
    angles = triangle_angles(A, B, C)
    angles_deg = [math.degrees(a) for a in angles]
    print(f"{name} angles (degrees): {angles_deg}") 
#----------------Task 3---------------------------------
# Inheriting from the parent vector class while overriding some methods in the new class
class ComplexVector(Vector):
	def __init__(self,x,y,z):
		self.x = complex(x)
		self.y = complex(y)
		self.z = complex(z)
#defining the complex magnitude method to overrride the one defined in the parent class which deals with real vectors
	def magnitude(self):
		return math.sqrt(abs(self.x)**2 + abs(self.y)**2+ abs(self.z)**2)
    # defining the complex dot profuct where we must find the complex conjugate of the first vector and multiply it by the other
	def scalar_product(self, other):
		return (self.x.conjugate()*other.x +
				self.y.comjugate()*other.y +
				self.x.conjugate()*other.z) 
# setting up the hansen vectors
k = Vector(0, 0, math.pi) 
kMag = k.magnitude()

#defining the vectors M and N prior to multiply by the pre factor exp(ikx) 
ex = ComplexVector(1, 0, 0) 
ey = ComplexVector(0, 1, 0) 

# computing the phase factor at position x, exp(ikx), to compute the vector fields M(x) and N(x) 
def phase(x):
    k_dot_x = k.scalar_product(x)
    return cmath.exp(1j *k_dot_x)

#defining the vector fields M and N 
def M_field(x):
	return phase(x) * ex 
def N_field(x): 
	return phase(x) * ey 

#finding the divergence of the vector fields and showing that they are equivalent to 0
def divergence_of_a(a,x): 
	k_dot_a = (k.x * a.x + k.y * a.y + k.z * a.z)
	return 1j * k_dot_a *phase(x) 

# finding the curl 
def curl_of_a(a,x):
	k_vec = ComplexVector(k.x, k.y, k.z) 
	return 1j * (k_vec.cross_product(a)) * phase(x)
# Evaluating the vector fields at a selected point in space and comparing the divergence and curl relations
# evaulating the hansen vectors at point in space
def check_properties(x):
	Mx = M_field(x)
	Nx = N_field(x)

	# finding the divergence for each vector which should both be zero 
	divM = divergence_of_a(ex, x)
	divN = divergence_of_a(ey, x)

	# curls of the teo vector fields 
	curlM = curl_of_a(ex, x)
	curlN = curl_of_a(ey, x) 

	# building the RHS for the relations stated in the assignment
	RHS_curlM = (1.0 / kMag) * Mx 
	RHS_curlN = (1.0 / kMag) * Nx

	# plane wave 
	RHS_curlM_pw = 1j * kMag * Nx 
	RHS_curlN_pw = -1j * kMag * Mx

	# mismathch error to verify the left and right hand sides of the relation
	err_mismatch_curlM = (curlM - RHS_curlM).magnitude()
	err_mismatch_curlN = (curlN - RHS_curlN).magnitude()
	err_mismatch_curlM_pw = (curlM - RHS_curlM_pw).magnitude()
	err_mismatch_curlN_pw = (curlN - RHS_curlN_pw).magnitude()					  

	# printing the test spatial point 
	print(f"Point x = ({x.x:.3f}, {x.y:.3f}, {x.z:.3f})")

	# printing the curl checks that we defined under the check-properties function 
	print("Curl checks:")
	print(f"  |curl M - N/|k||     = {err_mismatch_curlM:.3e}  (brief Eq. 2.8)")
	print(f"  |curl N - M/|k||     = {err_mismatch_curlN:.3e}  (brief Eq. 2.7)")
	print(f"  |curl M - N * |k||   = {err_mismatch_curlM_pw:.3e}  (planewave case)")
	print(f"  |curl N - M * |k||   = {err_mismatch_curlN_pw:.3e}  (planewave case)")

	# divergence checks 
	print("Divergence checks:")
	print(f"   |div M| = {abs(divM):.3e}")
	print(f"   |div N| = {abs(divN):.3e}")
	print()
# defining a loop which check the properties at different points manuallyt defined
if __name__ == "__main__":
	points = [
		Vector(0, 0, 0), 
	Vector(0, 0, 0.5), 
	Vector(0, 0, 1.0), 
	Vector(1.2, -0.7, 0.3)]

	for p in points: 
		check_properties(p)
	
	
	
	
	


