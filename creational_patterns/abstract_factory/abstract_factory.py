from abc import ABC, abstractmethod

#abstract class -> general base class for all the class
#concrete class -> system specific class that implements the abstract class


# Abstract Product A
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Product A for Windows
class WindowsButton(Button):
    def render(self):
        print("Rendering a button in Windows style")

# Concrete Product A for Linux
class LinuxButton(Button):
    def render(self):
        print("Rendering a button in Linux style")

# Abstract Product B
class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Product B for Windows
class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering a checkbox in Windows style")

# Concrete Product B for Linux
class LinuxCheckbox(Checkbox):
    def render(self):
        print("Rendering a checkbox in Linux style")

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factory for Windows
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Concrete Factory for Linux
class LinuxFactory(GUIFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()

# Client code
def create_gui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()

# Usage
if __name__ == "__main__":
    windows_factory = WindowsFactory()
    create_gui(windows_factory)

    linux_factory = LinuxFactory()
    create_gui(linux_factory)