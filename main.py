# Custom Imports
from dillionMath import Vector3, RotationMatrix
from pygame_utils.warp import warp as ImageWarpPygame

# Imports
import pygame
import numpy as np
import random
import pywavefront

pygame.init()
SCREEN_SIZE = (1920, 1080)
screen = pygame.display.set_mode(SCREEN_SIZE)
camera_position: Vector3 = Vector3.zero()

WHITE_COLOR = (255,255,255)

def toPyGameCords(x: float|list|tuple = 0, y: float = 0, z: float = 0):
    if isinstance(x, (list, tuple)):
        y = x[1]
        x = x[0]
    
    # This code moves to the Origin to the center of the screen
    return (
        (SCREEN_SIZE[0]/2) - x,
        (SCREEN_SIZE[1]/2) - y,
    )

class PolygonFacedObject():
    def __init__(self, vertices: list[Vector3] = None, faces: list[tuple[int, int]] = None, rotation: list[float,float,float] = [0,0,0], scale: float = 1, position: Vector3 = Vector3.zero()) -> None:
        if vertices == None or faces == None:
            vertices = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
            faces = [(0, 1), (0, 2), (2, 3), (1, 3), (4, 5), (4, 6), (6, 7), (5, 7), (0, 4), (1, 5), (2, 6), (3, 7)]
        
        self.vertices = np.array(vertices)
        self.faces = faces
        self.rotation = rotation
        self.scale = scale
        self.position = position
        
        self.color = WHITE_COLOR
        
        self.randomEdge = []
        for i in range(len(faces)):
            self.randomEdge.append((
                random.randint(0,len(vertices)-1),
                random.randint(0,len(vertices)-1)
            ))
    
    def tick(self):
        r = 0.05 / 25
        #r=0
        
        self.rotation[0] += r
        self.rotation[1] += r/2
        self.rotation[2] += r/3
    
    def fit(self, vec):
        return [round(70 * coordinate + frame / 2) for coordinate, frame in zip(vec, screen.get_size())]
    
    def draw(self):
        location = self.vertices.dot(RotationMatrix(*self.rotation))  # an index->location mapping
        #out = ((location[v1], location[v2]) for v1, v2 in self.edges)
        out = []
        for face in self.faces:
            out.append([])
            for point in face:
                out[-1].append(location[point])
        
        faceIndex = 0
        faceColors = [
            (51, 204, 51),      # Front - Green
            (0, 102, 255),      # Back - Blue
            (255, 153, 0),      # Left - Orange
            (204, 0, 0),        # Right - Red
            (255, 255, 255),    # Up - White
            (255, 255, 0),      # Down - Yellow
        ]
        
        #faceColors[0] = (255,255,255)
        #faceColors[1] = (255,255,255)
        #faceColors[2] = (255,255,255)
        #faceColors[3] = (255,255,255)
        #faceColors = [(255,255,255), (255,255,255), (255,255,255), (255,255,255), (255,255,255), (255,255,255)]
        
        for face in out:
            newFace = []
            for point in face:
                p = Vector3.toVector3(point)
                p *= self.scale
                p += self.position
                pointAsTuple = Vector3.toTuple(p)
                pointAsTuple = (pointAsTuple[0], pointAsTuple[1])
                pyGameTuple = toPyGameCords(pointAsTuple)
                
                newFace.append( pyGameTuple ) # was pointAsTuple
                #newFace.append(self.fit( point ))
            
            pygame.draw.polygon(screen, self.color, newFace, 4)
            #pygame.draw.polygon(screen, faceColors[faceIndex], newFace, 0)
            
            faceIndex += 1


obj = PolygonFacedObject(
    [(-1,-1,-1), (-1,-1,1), (-1,1,-1), (-1,1,1),   (1,-1,-1), (1,-1,1), (1,1,-1), (1,1,1)],
    [(0,1,3,2), (4,5,7,6), (0,1,5,4), (2,3,7,6), (0,4,6,2), (1,3,7,5) ],
    # Front,     Back,     Left,       Right,      Up,     Down
    
    [45, 45, 0],
    10,
    Vector3.forwards() * 10
)

while True:
    screen.fill((0,0,0))
     
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
    
    
    obj.draw()
    obj.tick()
    
    pygame.display.update()