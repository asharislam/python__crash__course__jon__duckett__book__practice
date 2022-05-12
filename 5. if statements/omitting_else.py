age = int(input("please enter your age:"))
if age <= 4:
    price =100

elif age <= 18:
    price = 200

elif age <= 65:
    price = 300

elif age <= 80:
    price = 400

print(f"your admission cost is ${price}.")

