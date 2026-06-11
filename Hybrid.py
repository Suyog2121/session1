# Hybrid Inheritance
class parent1:
    parentCar1= 'BMW'

class parent2:
    parentCar2 = 'Mercedes'

class child1(parent1, parent2):
    child1Car = 'kia'

objChild1 = child1()
print(objChild1.child1Car)
print(objChild1.parentCar1)

class child2(parent1, parent2):
    child2Car = 'alto'

objChild2 = child2()
print(objChild2.child2Car)
print(objChild2.parentCar2)
