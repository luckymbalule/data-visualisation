"""Contains Die class to generate random die roll"""
from random import randint


class Die:
    """Generates random die roll"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)