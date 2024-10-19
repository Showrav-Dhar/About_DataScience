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


# 5. Polymorphism Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar
# classes, but with different behaviors.
