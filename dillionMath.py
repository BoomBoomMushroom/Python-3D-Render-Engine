import math
import numpy as np

class Vector3:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    # Main Funcs
    def magnitude(self) -> float:
        return math.abs( math.sqrt( self.x**2 + self.y**2 + self.z**2 ) )
    
    def distance(self, vecB = None) -> float:
        if vecB == None or type(vecB) != Vector3: return None
        return math.sqrt( math.pow(self.x + vecB.x, 2) + math.pow(self.y + vecB.y, 2) + math.pow(self.z + vecB.z, 2) )



    def toTuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)
    
    def toVector3(toConvert: list | tuple[float, float, float] = [0,0,0]):
        return Vector3(toConvert[0], toConvert[1], toConvert[2])

    def toNumpy(self):
        return np.array(self.toTuple())

    # Dunder Methods
    def __add__(self, other = None):
        if type(other) != Vector3: raise TypeError("Can only add Vector3 to Vector3")
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other = None):
        if type(other) != Vector3: raise TypeError("Can only subtract Vector3 from Vector3")
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other = None):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (float, int)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        raise TypeError("Can only multiply Vector3 with other Vector3, ints, and floats")

    def __str__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __iter__(self):
        return iter((self.x, self.y, self.z))
    
    def __neg__(self):
        return self * -1

    # Variables
    # can't use "@property" because python doesn't seem to recognize it :/
    def zero():
        return Vector3(0,0,0)
    def left():
        return Vector3(-1,0,0)
    def right():
        return Vector3(1,0,0)
    def up():
        return Vector3(0,1,0)
    def down():
        return Vector3(0,-1,0)
    def forwards():
        return Vector3(0,0,1)
    def back():
        return Vector3(0,0,-1)

def RotationMatrix(alpha, beta, gamma):
    """
    rotation matrix of Alpha (α), Beta (β), and Gamma (γ) radians around x, y, z axes (respectively)
    """
    sAlpha, cAlpha = math.sin(alpha), math.cos(alpha)
    sBeta, cBeta = math.sin(beta), math.cos(beta)
    sGamma, cGamma = math.sin(gamma), math.cos(gamma)
    return (
        (cBeta*cGamma, -cBeta*sGamma, sBeta),
        (cAlpha*sGamma + sAlpha*sBeta*cGamma, cAlpha*cGamma - sGamma*sAlpha*sBeta, -cBeta*sAlpha),
        (sGamma*sAlpha - cAlpha*sBeta*cGamma, cAlpha*sGamma*sBeta + sAlpha*cGamma, cAlpha*cBeta)
    )
    
    # From https://stackoverflow.com/questions/21019471/how-can-i-draw-a-3d-shape-using-pygame-no-other-modules
    # Answer by Nitsan BenHanoch

"""
def RotatePoint(point, rotation):
    point_vector = point.toNumpy()
    rotation_matrix = RotationMatrix(*rotation)
    rotated_point = [
        sum(rotation_matrix[i][j] * point_vector[j] for j in range(3))
        for i in range(3)
    ]
    return Vector3.toVector3(rotated_point)
"""


def RotatePoint(point, rotation, center):
    # Step 1: Translate point and center to the origin
    point_vector = point.toNumpy() - center.toNumpy()
    
    # Step 2: Perform the rotation around the origin
    rotation_matrix = RotationMatrix(*rotation)
    rotated_point = [
        sum(rotation_matrix[i][j] * point_vector[j] for j in range(3))
        for i in range(3)
    ]
    
    # Step 3: Translate the result back to its original position
    rotated_point = Vector3.toVector3(rotated_point) + center
    
    return rotated_point


