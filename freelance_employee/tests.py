# from django.test import TestCase

# Create your tests here.
# OOPs concept
# boks, pencils etc..

# principles
# 1. class
# 2. objects
# 3. Method
# 4. Inheritance
# 5. Polymorphism
# 6. data abstraction
# 7. Encapsulation

# class
# atrribute and methods

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display(self):
        print(self.model, self.year)


c = Car('toyota', 2022)
c.display()
