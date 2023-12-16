# Day 4: Dec 15, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 04:51:45 - go to 14_average.py

# import everythings in random module
import random

# import only choice from random
# we can import any function from any module using from _ import _
# to import like this you don't have to use random.choice but choice only instead
from random import choice

# random.choice
coin_list = ["heads", "tails"]
coin = random.choice(coin_list)
print(coin)

# choice from random
print()
coin = choice(coin_list)
print(coin)

# random.randint
print()
number = random.randint(1, 15)
print(number)

# random.shuffle
print()
cards_list = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
random.shuffle(cards_list)
for c in range(len(cards_list)):
        print(cards_list[c])