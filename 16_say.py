# Day 4: Dec 15, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From continue to 17_itunes.py (for working with APIs)

import cowsay
import sys

if len(sys.argv) == 2:
        # this will display the cow to say Hello, (name)
        cowsay.cow("Hello, " + sys.argv[1])
        # this will display the trex to say Hello, (name)
        cowsay.trex("Hello, " + sys.argv[1])