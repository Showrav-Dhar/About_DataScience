# # Create a Car class with attributes like brand and model. Then create an instance of this class.
# class Car:
#
#     # have to pass [self] keyword every time you create a function inside a class
#     def __init__(self, brand, model):  # constructor
#         self.brand = brand
#         self.model = model
#
#     def details(self):
#         print(f"Brand Name = {self.brand} , Car Model - {self.model}")
#
#
# # car1 = Car("Toyota", "Noah")
# # print(car1.brand)
# #
# # car2 = Car("Mercedes", "AMG")
# # print(car2.brand)
#
# # question2
# # car3 = Car("Mazda", "Axela")
# # print(car3.details())
#
#
# # Problem3: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, batterySize):
#         super().__init__(brand, model)
#         self.batterySize = batterySize
#
#
# # EV1 = ElectricCar("Tesla", "Mark10", "85 KwH")
# # EV1.details()
#
# # Problem4: Modify the Animal class to encapsulate the brand attribute, making it private, and provide a getter method
# # for it.
#
# class Animal:
#     def __init__(self, Name, Age):
#         self.__Name = Name  # to make Name attribute private , two underscore is given before Name attribute
#         self.Age = Age
#
#     def get_name(self):
#         return self.__Name + " !" #made name attribute private
#
#     def details(self):
#         print(f"Type = {self.__Name}, Name = {self.Age}")
#
#
# class dog(Animal):
#
#     def __init__(self, Name, Age, Type):
#         super().__init__(Name, Age)
#         self.Type = Type
#
#
# # d1 = dog("Tommy", 20, "Dog")
# # print(d1.__Name)
#
# d1 = Animal("Tommy", 20)
# print(d1.__Name)

# class computer:
#     def __init__(self):
#         self.__maxprice = 1000
#
#     def sellingPrice(self):
#         print(f"Selling price = {self.__maxprice}")
#
#     def priceSetter(self,price):
#         self.__maxprice = price
#
#
# c = computer()
# c.priceSetter(1500)
# c.sellingPrice()


# 5. Polymorphism Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar
# classes, but with different behaviors.

# class Car:
#
#     # have to pass [self] keyword every time you create a function inside a class
#     def __init__(self, brand, model):  # constructor
#         self.brand = brand
#         self.model = model
#
#     def details(self):
#         print(f"Brand Name = {self.brand} , Car Model - {self.model}")
#
#     def fuel_type(self):
#         print(f"Fule type = Disel")
#
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, batterySize):
#         super().__init__(brand, model)
#         self.batterySize = batterySize
#
#     def fuel_type(self):
#         print(f"Fule type = Electric Charge")
#
#
# car1 = Car("Toyota", "Corolla")
#
# ev1 = ElectricCar("Tesla", "Model X", 100000)
#
# ev1.fuel_type()
# car1.fuel_type()

# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

# class Car:
#     total_cars = 0
#
#     # have to pass [self] keyword every time you create a function inside a class
#     def __init__(self, brand, model):  # constructor
#         self.brand = brand
#         self.model = model
#         self.total_cars += 1
#
#     def details(self):
#         print(f"Brand Name = {self.brand} , Car Model - {self.model}")
#
#     def fuel_type(self):
#         print(f"Fule type = Disel")
#
#
# car1 = Car("Tata", "Nexon")
# car2 = Car("Tata", "Alto")
# car3 = Car("Tata", "OMNI")
# print(Car.total_cars)


# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

# class Bike:
#
#     def __init__(self, Brand, Name):
#         self.Brand = Brand
#         self.Name = Name
#
#     @staticmethod
#     def general_description():
#         return "Bike is Two Wheeler"
#
#
# b1 = Bike("Pulser", "Bajaj")
# print(Bike.general_description())


# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

# class Car:
#     def __init__(self, Model, Brand):
#         self.__Model = Model
#         self.Brand = Brand
#
#     def full_name(self):
#         print(f"Car Model = {self.__Model} , Brand = {self.Brand}")
#
#     @property
#     def Model(self):
#         return self.__Model
#
#
# c1 = Car("Axela", "Mazda")
# print(c1.Model)

# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
# class Car:
#
#     # have to pass [self] keyword every time you create a function inside a class
#     def __init__(self, brand, model):  # constructor
#         self.brand = brand
#         self.model = model
#
#     def details(self):
#         print(f"Brand Name = {self.brand} , Car Model - {self.model}")
#
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, batterySize):
#         super().__init__(brand, model)
#         self.batterySize = batterySize
#
#
# my_tesla = ElectricCar("Tesla", "Mark10", "85 KwH")
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))


# 10. Multiple InheritanceProblem: Create two classes Battery and Engine,
# and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
class Father:
    def Father_info(self):
        print("Father - Russo")

class Mother:
    def Mother_info(self):
        print("Mother - Zoe")

class Boy_Child(Father, Mother):
    pass

b1 = Boy_Child()

b1.Father_info()
b1.Mother_info()
