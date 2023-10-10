import math

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
        return tuple(self.x, self.y, self.z)

    # Dunder Methods
    def __add__(self, other = None):
        if type(other) != Vector3: raise TypeError("Can only add Vector3 to Vector3")
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other = None):
        if type(other) != Vector3: raise TypeError("Can only subtract Vector3 from Vector3")
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    # Variables
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

