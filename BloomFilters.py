"""
Bloom Filters are lightweight Hash Tables that make use of probablistic lookups.
It might give you "false positives" i.e. might return true even if an object might 
not be present within it.
However, it will never give you a "false negative".
"""

# Pokedex Bloom Filter:

import pyhash

bit_vector = [0] * 20

fnv_pika = fnv("Pikachu") % 20
fnv_charmander = fnv("Charmander") % 20

murmur_pika = murmur("Pikachu") % 20
murmur_charmander = murmur("Charmander") % 20

bit_vector[fnv_pika] = 1
bit_vector[fnv_charmander] = 1
bit_vector[murmur_pika] = 1
bit_vector[murmur_charmander] = 1
