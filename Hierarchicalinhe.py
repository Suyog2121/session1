# Hierarchical Inheritance
class Parent:
    parentCar1 = 'BMW'
    parentCar2 = 'Mercedes'

class Child1(Parent):
    child1Car = 'kia'

objChild1 = Child1()
print(objChild1.child1Car)
print(objChild1.parentCar1)

class Child2(Parent):
    child2Car = 'alto'

objChild2 = Child2()
print(objChild2.child2Car)
print(objChild1.parentCar2)

