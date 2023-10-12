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
  