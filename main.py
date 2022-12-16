"""Where will be some beautiful code"""
from dataclasses import dataclass


@dataclass
class Animals():
    healt: int = 100


@dataclass
class Wolf(Animals):
    hungry: int = 5
    speed: int = 5
    force: int = 5
    voice: str = ('vuuuuu',)
