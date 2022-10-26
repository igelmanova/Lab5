class figColor():
    def __init__(self, color):
        self.color = color

class rectangle(figColor):
    def __init__(self, width, height, color='red'):
        self.width = width
        self.height = height
        self.color = figColor(color)
    
    def getSquare(self):
        return (self.width * self.height)
    
    def repr(self):
        return (self.width, self.height, self.color.color, self.getSquare())
        
class circle():
    def __init__(self, radius):
        self.radius = radius
        
    def getSquare(self):
        return (self.radius * math.pi)
    
    def repr(self):
        return (self.radius, self.color, self.getSquare())

class square(rectangle):
    def __init__(self, side):
        self.side = rectangle(side, side)
    
    def repr(self):
        return (self.side.width, self.side.color.color, self.side.getSquare())

a = rectangle(2, 3, 'red')
b = square(2)
print(b.repr())
    
    
