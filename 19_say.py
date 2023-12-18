# Day 4: Dec 15, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 06:00:15 - 06:09:15
import sys

from sayings_19_say import hello
from sayings_19_say import goodbye

if len(sys.argv) == 3:
        hello(sys.argv[1])
        goodbye(sys.argv[2])