def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, "pepperon1")
make_pizza(12, "mashrooms", "green peppers", "extra cheese")