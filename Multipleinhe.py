# Multiple Inheritance
class Parent1:
    parent1Car = 'BMW'

class Parent2:
    parent2Car = 'Mercedes'

class Child(Parent1, Parent2):
    childCar = 'kia'

objChild = Child()
print(objChild.childCar)
print(objChild.parent1Car)
print(objChild.parent2Car)
