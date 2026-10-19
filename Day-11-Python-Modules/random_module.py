# Day 11: Python Random Module

import random

print("Random number:", random.randint(1, 100))

colors = ["Red", "Blue", "Green", "Yellow"]

print("Random color:", random.choice(colors))

random.shuffle(colors)
print("Shuffled colors:", colors)
