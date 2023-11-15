#single inheritance


class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Cat(Animal):
    def __init__(self,name,sound,color):
        super().__init__(name,sound)
        self.color = color
    def show_color(self):
        print(f"{self.name} is {self.color}")
cat = Cat("Reo","meow","white")
cat.make_sound()
cat.show_color() 

# multilevel inheritance
class Parent:
    def __init__(self,str1):
       self.str1 = str1
class Child(Parent):
    def surname(self):
        self.str2 = "Videm"
class Grand_child(Child):
    def name(self):
        print(self.str1 +" "+ self.str2)
p = Grand_child("Shireesha")
p.surname()
p.name()

# multiple inheritance
class SuperClass1:
    num1 = 3

class SuperClass2:
    num2 = 5

class SubClass( SuperClass1, SuperClass2):
    def addition(self):
        return self.num1 + self.num2

obj = SubClass()
print(obj.addition())

# Hierachial inheritance
class Shape:
    def __init__(self, color, area):
        self.color = color
        self.area = area
    def show(self):
        print(f"This shape is {self.color} and has an area of {self.area} square units")
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color, 3.14*radius**2)
        self.radius = radius
    def show_radius(self) :
        print(f"This circle has a radius of {self.radius} units")
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color, length*width)
        self.length = length
        self.width = width
    def show_dimensions(self):
        print(f"This rectangle has a length of {self.length} units and width of {self.width} units") 
circle = Circle("black", 3)
circle.show()
circle.show_radius()
rect = Rectangle("blue", 2, 4) 
rect.show()
rect.show_dimensions() 

# Hybrid inheritance
class Vehicle:
    def __init__(self, name, speed):
       self.name = name
       self.speed = speed
    def show(self):
        print(f"This vehicle is {self.name} and has a speed of {self.speed} km/h")
class Electric:
    def __init__(self, power):
        self.power = power
    def show_power(self):
        print(f"This vehicle has a power of {self.power} kWh")
class Car(Vehicle):
    def __init__(self, name, speed, color):
        super().__init__(name, speed)
        self.color = color
    def show_color(self):
        print(f"This car is in {self.color}")
class Bike(Vehicle):
    def __init__(self, name, speed, type):
        super().__init__(name, speed)
        self.type = type
    def show_type(self):
        print(f"This bike is {self.type}")
class Tesla(Car,Electric):
    def __init__(self, name, speed, color, power, model):
        Car.__init__(self, name, speed, color)
        Electric.__init__(self,power)
        self.model = model
    def show_model(self):
        print(f"Tesla is {self.model}")
tesla = Tesla("Tesla", 200, "grey", 100,"Model 2")
tesla.show()
tesla.show_color()
tesla.show_power() 
tesla.show_model()
           
