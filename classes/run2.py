#!/usr/bin/env python

from backpacks import Rucksack

myrucksack = Rucksack('Crumpler', 'green', 6)

print('My rucksack is', myrucksack.color)
print('My rucksack has volume', myrucksack.volume())
print('My rucksack has length', len(myrucksack))

if myrucksack.fashionable():
    print('My rucksack is fashionable!')
else:
    print('My rucksack is unfortunately not fashionable :-(')

if myrucksack.waterproof:
    print('My rucksack is waterproof!')
else:
    print('My rucksack is unfortunately not waterproof :-(')
