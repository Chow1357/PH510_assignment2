#!/opt/software/anaconda/python-3.10.9/bin/python
"""
using Object Oriented Programming (OOP) logic to create
classes which can be used for vector calculations

Tested using:
    Python 3.10.9
"""
#defining the required math functions for regular operations and for handling complex functions
import cmath
import math

#defining a function to title each section of results
def print_title(title):
    """ prints a title for each task """
    print("\n" + "=" * 50)
    print(f"{title:^50}") # Center title
    print("=" * 50)

# defining the new parent class called vector
class Vector:
    """
    Represents a 3D cartesian Vector

    which supports addition, subtraction, scalar multiplication,
    dot product, cross product and magnitude computation.
    """

    def __init__(self, x, y, z): # initialise vector components
        self.x = x
        self.y = y
        self.z = z
    # prints the vector in the form required
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    # defines the method for adding vectors
    # adds two vectfors and returns a resulting vector as an instance
    def __add__(self, other):
        return self.__class__(self.x + other.x,self.y + other.y, self.z + other.z)

    #same method for addition but using sub instead
    def __sub__(self, other):
        return self.__class__(self.x - other.x,self.y - other.y, self.z - other.z)

    #defining scalar multiplication
    def __mul__(self, a):
        if isinstance(a, (int, float, complex)):
            return self.__class__(
                a * self.x,
                a * self.y,
                a * self.z)
        return NotImplemented
    # ensures that python can do both 2 * v as well as v * 2
    __rmul__ = __mul__

    # defining the function to find the magnitude of a real vector
    def magnitude(self):
        """Returns the magnitude of the vector"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # function to calculate scalar product
    def scalar_product(self, other):
        """finds the scalar product of two vectors"""
        return self.x*other.x + self.y*other.y + self.z*other.z

    # cross product function
    def cross_product(self, other):
        """Finds the cross product of two vectors"""
        return self.__class__(self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
                self.x*other.y - self.y*other.x)

#title for task 1 results
print_title("Task 1: basic vector operations using a parent class")
# using the object class
#creating the vector objects
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

#testing the add and subtract methods inside the parent class
#and returning two new vector objects v3 and v4
v3 = v1 + v2
v4 = v2 - v1

print(v1) # prints the vector v1 (1, 2, 3)
print("sum of v1 and v2:", v3)
print(" subtracting v1 from v2:", v4)
print("cross product between v1 and v2:", v1.cross_product(v2))
print("scalar product between v1 and v2:", v1.scalar_product(v2))
print("Magnitude of v1:", v1.magnitude()) # computes the magnitude of vector v1

#-----------Task 2--------------------
#instantiate the vectors which represent the
#cartesian points for each triangle
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
def triangle_area(a, b, c):
    """finds the area of triangle ABC using the cross product"""
    ab = b - a
    ac = c - a
    return 0.5 * ab.cross_product(ac).magnitude()

#print the area of the four seperate triangles
print_title("Task 2a: areas of the four triangles")
print("Triangle 1 area:", triangle_area(A1, B1, C1))
print("Triangle 2 area:", triangle_area(A2, B2, C2))
print("Triangle 3 area:", triangle_area(A3, B3, C3))
print("Triangle 4 area:", triangle_area(A4, B4, C4))

#-----part B--------
#define the function to calculate the internal angles of the triangles
def angle_between(u, v):
    """finds the angle between two known vectors u and v"""
    dot = u.scalar_product(v)
    mag_u = u.magnitude()
    mag_v = v.magnitude()

    cos_theta = dot / (mag_u * mag_v)
    # clamp to avoid floating point errors beyond the range (-1,1)
    cos_theta = max(1.0, min(-1.0, cos_theta))

    return math.acos( dot / (mag_u * mag_v) )
# function that finds the edges of the triangle between
# which the internal angles are
def triangle_angles(a, b, c):
    """finds the edges that the three angles are between
       then computes the angle between the edges"""
    # finding the vectors that meet at the vertex or cartesian point A
    ab = b-a
    ac = c-a
    # same method for vertex B
    ba = a-b
    bc = c-b

    ca = a-c
    cb = b-c
    # calculating the angle between the defined vectors using the
    # angle between function we defined
    angle_a = angle_between(ab, ac)
    angle_b = angle_between(ba, bc)
    angle_c = angle_between(ca, cb)
    return angle_a, angle_b, angle_c
#storing the triangles
triangles = [("triangle_1", A1, B1, C1),
    ("triangle_2", A2, B2, C2),
    ("triangle_3", A3, B3, C3),
    ("triangle_4", A4, B4, C4)]

# title before results for part b
print_title("Task 2b: printing the internal angles of the four triangles")

# a for loop which goes through the four triangles and prints
# the internal angles using the edges we have defined
for name, A, B, C in triangles:
    angles = triangle_angles(A, B, C)
    angles_deg = [math.degrees(a) for a in angles]
    print(f"{name} angles (degrees): {angles_deg}")
#----------------Task 3---------------------------------
# Inheriting from the parent vector class while overriding some methods in the new class
class ComplexVector(Vector):
    """
    new vector class for dealing with complex functions

    inherits from the orginal vector class
    """
    def __init__(self,x,y,z):
        """initialise complex vector components"""
        super().__init__(complex(x),
        complex(y),
        complex(z))
#defining the complex magnitude method to overrride the one
#defined in the parent class which deals with real vectors
    def magnitude(self):
        """
        finds the magnitude when dealing with complex vectors
        """
        return math.sqrt(abs(self.x)**2 + abs(self.y)**2 + abs(self.z)**2)
    # defining the complex dot profuct where we must find the complex
    # conjugate of the first vector and multiply it by the other
    def scalar_product(self, other):
        """
        calculates the scalar product when complex vectors are involved
        """
        return (self.x.conjugate() * other.x +
                self.y.conjugate() * other.y +
                self.z.conjugate() * other.z)
# setting up the hansen vectors
k = Vector(0, 0, math.pi)
kMag = k.magnitude()

#defining the vectors M and N prior to multiply by the pre factor exp(ikx)
ex = ComplexVector(1, 0, 0)
ey = ComplexVector(0, 1, 0)

# computing the phase factor at position x, exp(ikx),
# to compute the vector fields M(x) and N(x)
def phase(x):
    """ defines the phase factor """
    k_dot_x = k.scalar_product(x)
    return cmath.exp(1j *k_dot_x)

#defining the vector fields M and N
def m_field(x):
    """__"""
    return phase(x) * ex
def n_field(x):
    """___"""
    return phase(x) * ey

#Alternative: approximate derivatives with central finite differences from Eq. 2.10
#Here in this example we evaluate div/curl analytically 
#since M and N are plane waves, a*exp(i k·x)
#using the identity; ∇ exp(i k·x) = i k exp(i k·x)
#we can avoid numerical approximation errors

#finding the divergence of the vector fields
def divergence_of_a(a,x):
    """finds the divergence"""
    k_dot_a = k.x * a.x + k.y * a.y + k.z * a.z
    return 1j * k_dot_a *phase(x)

# finding the curl
def curl_of_a(a,x):
    """computes the curl"""
    k_vec = ComplexVector(k.x, k.y, k.z)
    return 1j * k_vec.cross_product(a) * phase(x)
# Evaluating the vector fields at a selected point in
# space and comparing the divergence and curl relations
# title for task 3 results
print_title("Task 3: checking hansen vectors obey the conditions for certain test vectors")
def check_properties(x):
    """
    defines our method of checking that our hansen

    vectors obey the conditions
    """
    mx = m_field(x)
    nx = n_field(x)

    # finding the divergence for each vector which should both be zero
    divm = divergence_of_a(ex, x)
    divn = divergence_of_a(ey, x)

    # curls of the teo vector fields
    curlm = curl_of_a(ex, x)
    curln = curl_of_a(ey, x)

    # building the RHS for the relations stated in the assignment
    rhs_curlm = (1.0 / kMag) * nx
    rhs_curln = (1.0 / kMag) * mx
    # plane wave
    rhs_curlm_pw = 1j * kMag * nx
    rhs_curln_pw = -1j * kMag * mx

    # mismathch error to verify the left and right hand sides of the relation
    err_mismatch_curlm = (curlm - rhs_curlm).magnitude()
    err_mismatch_curln = (curln - rhs_curln).magnitude()
    err_mismatch_curlm_pw = (curlm - rhs_curlm_pw).magnitude()
    err_mismatch_curln_pw = (curln - rhs_curln_pw).magnitude()

    # printing the test spatial point
    print(f"Point x = ({x.x:.3f}, {x.y:.3f}, {x.z:.3f})")

    # printing the curl checks that we defined under the check-properties function
    print("Curl checks:")
    print(f"  |curl M - N/|k||     = {err_mismatch_curlm:.3e}  (brief Eq. 2.8)")
    print(f"  |curl N - M/|k||     = {err_mismatch_curln:.3e}  (brief Eq. 2.7)")
    print(f"  |curl M - i|k| * N|   = {err_mismatch_curlm_pw:.3e}  (planewave case)")
    print(f"  |curl N + i|k| * M|   = {err_mismatch_curln_pw:.3e}  (planewave case)")

    # divergence checks
    print("Divergence checks:")
    print(f"   |div M| = {abs(divm):.3e}")
    print(f"   |div N| = {abs(divn):.3e}")
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
