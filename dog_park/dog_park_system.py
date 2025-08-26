from typing import List

class Dog:
    def __init__(self, dog_id, age, size, is_vaxxed, cond):
        self.id = dog_id
        self.age = age
        self.size = size  # SMALL or LARGE
        self.is_vaxxed = is_vaxxed
        self.cond = cond  # e.g., "NORMAL", "SHEDDER"

class Playground:
    def __init__(self, size, cap):
        self.size = size
        self.cap = cap
        self.dogs = set()

    def can_accept(self, dog: Dog) -> bool:
        if dog.size != self.size: return False
        if not dog.is_vaxxed: return False
        if dog.age >= 10: return False
        if dog.cond == "SHEDDER": return False
        if len(self.dogs) >= self.cap: return False
        return True

    def add_dog(self, dog: Dog):
        self.dogs.add(dog)

    def remove_dog(self, dog: Dog):
        self.dogs.remove(dog)

class Facility:
    def __init__(self, playgrounds: List[Playground]):
        self.playgrounds = playgrounds

    def check_in(self, dog: Dog):
        for p in self.playgrounds:
            if p.can_accept(dog):
                p.add_dog(dog)
                print("Checked in:", dog.id)
                return
        print("Couldn't find a playground for dog", dog.id)

    def check_out(self, dog: Dog):
        for p in self.playgrounds:
            if dog in p.dogs:
                p.remove_dog(dog)
                print("Checked out:", dog.id)
                return
        print("Couldn't find dog:", dog.id)
