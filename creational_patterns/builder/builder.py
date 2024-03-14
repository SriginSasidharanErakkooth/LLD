class Pizza:
    def __init__(self):
        self.crust = None
        self.sauce = None
        self.toppings = []

    def __str__(self):
        return f"Crust: {self.crust}, Sauce: {self.sauce}, Toppings: {', '.join(self.toppings)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_crust(self, crust):
        self.pizza.crust = crust
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        return self.pizza


if __name__ == "__main__":
    pizza_builder = PizzaBuilder()
    pizza = pizza_builder.set_crust("Thin").set_sauce("Tomato").add_topping("Cheese").add_topping("Mushrooms").build()

    print(pizza)  # Output: Crust: Thin, Sauce: Tomato, Toppings: Cheese, Mushrooms
