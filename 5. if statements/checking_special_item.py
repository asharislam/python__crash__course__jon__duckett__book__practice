request_toppings = ["mushrooms", "green peppers", "extra cheese"]
for request_topping in request_toppings:
    print(f"Adding {request_topping}.")

print("\n Finishing making your pizza!")

#But what if the pizzeria runs out of 
# green peppers? An if statement inside 
# the for loop can handle this situation appropriately

request_toppings_1 = ["mushrooms", "green peppers", "extra cheese"]
for request_topping_1 in request_toppings_1:
    if request_topping_1 == "green pepers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {request_topping_1}.")
print("\n Finishing making your pizza")