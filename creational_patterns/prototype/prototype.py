#The Prototype Pattern is a creational design pattern that allows you 
# to create new objects based on an existing object, known as the prototype. 
# Here's a simple implementation of the Prototype Pattern in Python:


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def clone(self):
        return self

    def __str__(self):
        return f"Car [make={self.make}, model={self.model}, year={self.year}]"


if __name__ == "__main__":
    # Create prototype instances
    ford_prototype = Car("Ford", "Mustang", 2022)
    tesla_prototype = Car("Tesla", "Model S", 2023)

    # Clone and customize prototypes
    ford_clone = ford_prototype.clone()
    ford_clone.year = 2024

    tesla_clone = tesla_prototype.clone()
    tesla_clone.model = "Model X"

    # Output cloned cars
    print("Cloned Ford:", ford_clone)
    print("Cloned Tesla:", tesla_clone)
