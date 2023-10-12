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