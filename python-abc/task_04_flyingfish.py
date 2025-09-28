#!/usr/bin/env python3
"""
In some object-oriented languages, a class can inherit attributes and behaviors from more than one parent class.
"""


class Fish:
    """Create a Fish class with methods swim (which prints “The fish is swimming”) and habitat (which prints “The fish lives in water”)."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """Create a Bird class with methods fly (which prints “The bird is flying”) and habitat (which prints “The bird lives in the sky”).
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Implementing FlyingFish"""
    def fly(self):
        print("The flying fish is soaring!.")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
