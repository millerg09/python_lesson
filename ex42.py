## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-an Animal
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Cat is-an Animal
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Person is an object
class Person(object):
    def __init__(self, name):
        ## Person has a name
        self.name = name

        ## Person has a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee has a name
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## a fish is an object
class Fish(object):
    pass

## a salmon is a fish
class Salmon(Fish):
    pass

## a halibut is a fish
class Halibut(Fish):
    pass

### Instances

## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## satan is a pet of mary
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## rover is a pet of frank
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()
