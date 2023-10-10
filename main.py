# Custom Imports
from dillionMath import Vector3


# Imports
import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
camera_pos: tuple = (0, 0, 0)

class Point():
    def __init__(self, pos: tuple[float, float, float], color: tuple[int, int, int, int] = (255, 255, 255, 255)) -> None:
        self.pos = pos
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

wireframes: list[Wireframe] = []

wireframes.append(Wireframe([

]))

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
    for i in wireframes:
        i.tick()