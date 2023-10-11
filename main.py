# Custom Imports
from dillionMath import Vector3, RotationMatrix
from pygame_utils.warp import warp as ImageWarpPygame

# Imports
import pygame
import numpy as np
import random
import pywavefront

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
#screen = pygame.display.set_mode((450,450))
camera_position: tuple = (0, 0, 0)

WHITE_COLOR = (255,255,255,255)

class Point():
    def __init__(self, position: tuple[float, float, float], color: tuple[int, int, int, int] = (255, 255, 255, 255)) -> None:
        if type(position) == Vector3: position = position.toTuple()
        
        self.position = position
        self.color = color

    def tick(self) -> None:
        pass

class Edge():
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def tick(self) -> None:
        self.start.tick()
        self.end.tick()

class Wireframe():
    def __init__(self, edges: list[Edge]) -> None:
        self.edges: list[Edge] = edges

    def tick(self) -> None:
        for i in self.edges:
            i.tick()





class Object():
    def __init__(self, vertices: list[Vector3] = None, edges: list[tuple[int, int]] = None) -> None:
        if vertices == None or edges == None:
            vertices = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
            edges = [(0, 1), (0, 2), (2, 3), (1, 3), (4, 5), (4, 6), (6, 7), (5, 7), (0, 4), (1, 5), (2, 6), (3, 7)]
        
        self.vertices = np.array(vertices)
        self.edges = edges
        self.rotation = [0, 0, 0]
        
        self.randomEdge = []
        for i in range(len(edges)):
            self.randomEdge.append((
                random.randint(0,len(vertices)-1),
                random.randint(0,len(vertices)-1)
            ))
    
    def tick(self):
        r = 0.05 / 25
        
        self.rotation[0] += r
        self.rotation[1] += r/2
        self.rotation[2] += r/3
    
    def fit(self, vec):
        return [round(70 * coordinate + frame / 2) for coordinate, frame in zip(vec, screen.get_size())]
    
    def draw(self):
        location = self.vertices.dot(RotationMatrix(*self.rotation))  # an index->location mapping
        out = ((location[v1], location[v2]) for v1, v2 in self.edges)
        
        outList = []
        
        for start, end in out:
            a = self.fit(start)
            b = self.fit(end)
            
            outList.append(a)
            outList.append(b)
            pygame.draw.line(screen, (255, 128, 128), a, b, 4)
        
        


wireframes: list[Wireframe] = []

obj = Object(
    [(-1,-1,-1), (-1,-1,1), (-1,1,-1), (-1,1,1),   (1,-1,-1), (1,-1,1), (1,1,-1), (1,1,1)],
    [(0,1),(0,2),(1,3),(2,3),  (0,4),(1,5),(2,6),(3,7),  (4,5),(4,6),(5,7),(6,7)],
)

while True:
    screen.fill((0,0,0))
     
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
    
    """
    for i in wireframes:
        i.tick()
    """
    
    
    obj.draw()
    obj.tick()
    
    pygame.display.update()