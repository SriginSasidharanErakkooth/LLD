#Factory Method is a creational design pattern that provides an interface for creating 
# objects in a superclass, but allows subclasses to alter the type of objects that will
# be created.

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Invalid shape type")

# Usage
factory = ShapeFactory()
circle = factory.create_shape("circle")
circle.draw()  # Output: Drawing a circle

rectangle = factory.create_shape("rectangle")
rectangle.draw()  # Output: Drawing a rectangle