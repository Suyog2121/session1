# Single Inheritance
class Parent:
    parentCar = 'BMW'

class Child(Parent):
    childCar = 'alto'
objC = Child()
print(objC.parentCar)
print(objC.childCar)
