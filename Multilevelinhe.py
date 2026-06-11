# Multilevel Inheritance
class grandParent:
    grandParentBike = 'Rajdoot'

class Parent(grandParent):
    parentCar = 'BMW'

class Child(Parent):
    childCar = 'alto'
objC = Child()
print(objC.grandParentBike)
print(objC.parentCar)
print(objC.childCar)
