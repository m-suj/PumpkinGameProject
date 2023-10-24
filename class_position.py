class Vector:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
