from math import hypot
from random import random

def distance(p, q):
    xp, yp = p
    xq, yq = q
    return math.sqrt((xq-xp)**2 + (yq-yp)**2)

def average(n):
    avg = 0
    for i in range(n):
        p = (random(), random())
        q = (random(), random())
        avg += distance(p, q)/n

    return avg

def average2(n):
    avg = 0
    for i in range(n):
        p = (random(), random())
        q = (random(), random())
        avg += distance(p, q)

    return avg/n