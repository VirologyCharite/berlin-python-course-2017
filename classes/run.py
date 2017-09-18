#!/usr/bin/env python

from backpacks import Bag

mybag = Bag(color='green', model='Crumpler', pockets=4, depth=3)

print('My bag has volume', mybag.volume())

if mybag.fashionable():
    print('My bag is fashionable!')
else:
    print('My bag is unfortunately not fashionable :-(')
