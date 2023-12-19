# Day 5: Dec 18, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 08:25:00

# install pillow use: python3 -m pip install pillow
# There is a bug the gif display 2 images at the same time

import sys
from PIL import Image

def main():
        image()

def image():

        images = []
        for arg in sys.argv[1:]:
                image = Image.open(arg)
                images.append(image)
        images[0].save(
                "pikachu/pikachu.gif", format="GIF", append_images=[images[1]], save_all=True, duration=200, loop=0
        )

if __name__ == "__main__":
        main()

