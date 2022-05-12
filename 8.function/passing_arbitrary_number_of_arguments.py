"""def make_pizza(*toppings):
    print(toppings)
make_pizza("pepperson1")
make_pizza("mushrooms", "green peppers", "extra cheese")"""

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza("pepperon1")
make_pizza("mushrooms", "green peppers", "extra cheese")

