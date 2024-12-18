import pygame


import pygame 
import math

class Vector2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001

def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

def __sub__(self, other):
    return Vector2(self.x - other.x, self.y - other.y)

def __neg__(self):
    return Vector2(-self.x, -self.y)

def __mul__(self, scalar):
    return Vector2(self.x * scalar, self.y * scalar)

def __div__(self, scalar):
    if scalar != 0:
        return Vector2(self.x / float(scalar), self.y / float(scalar))
    return None

def __truediv__(self, scalar):
    return self.__div__(scalar)