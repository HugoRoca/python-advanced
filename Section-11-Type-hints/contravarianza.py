from typing import Tuple


# supertype
class Animal:
    ...


# subtype
class Dog(Animal):
    ...


animal_1: Animal = Animal()

dog1: Dog = Dog()
dog2: Dog = Dog()

animals: Tuple[Animal, ...] = (animal_1, dog1)
dogs: Tuple[Dog, ...] = (dog1, dog2)