import pizza as p

p.make_pizza(16, "pepperson1")
p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# importing all functions in a module

from pizza import *
make_pizza(13, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")