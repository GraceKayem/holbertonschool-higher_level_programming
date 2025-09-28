#!/usr/bin/env python3
"""
Mixins are a way to add functionality to classes in a modular fashion. They’re not meant to stand alone but are meant to be combined with other classes to add behaviors. 
"""


class SwimMixin:
    """Design two mixin classes, SwimMixin and FlyMixin, each equipped with methods swim and fly respectively."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin that adds flying ability."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from SwimMixin and FlyMixin."""
    def roar(self):
        print("The dragon roars!")
