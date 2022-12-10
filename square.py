class Point:
    def __init__(self, x, y, z) :
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        X = self.x * self.x
        Y = self.y * self.y
        Z = self.z * self.z
        return(X + Y + Z)

data = Point(1, 3, 5)
print(data.sqSum())
