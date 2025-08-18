
class Shape:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled is True else 'Not Filled'}")
class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius
    def describe(self):
        print(f"It is circle with an area of {3.14 * self.radius ** 2} cm^2")
        super().describe()
        
class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width = width
    def describe(self):
        print(f"It is square with an area of {self.width ** 2} cm^2")
        super().describe()
class Triangle(Shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It is triangle with an area of {(self.width * self.height) / 2} cm^2")
        super().describe()  
        
        
circle = Circle(color="red",filled=True,radius=5)
square = Square(color="blue",filled=False,width=6)
triangle = Triangle(color="Green",filled=True,width=5,height=6)
print(circle.color)
print(circle.filled)
print(circle.radius)

print(square.color)
print(square.filled)
print(square.width)

circle.describe()
square.describe()
triangle.describe()
