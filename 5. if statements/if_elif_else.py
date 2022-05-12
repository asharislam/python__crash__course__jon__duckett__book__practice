"""#admission cost with age
age = int(input("please enter your age: "))
if age <= 4:
    print("your admission cost is free.")
elif age <= 18:
    print(" your admission cost is 18$")
else:
    print("you are adult and your admision coast is 40$")
"""
#price base
age_1 = int(input("please enter your age: "))
if age_1 >=4:
    price = 0
elif age_1 >=18:
    price = 25
else:
    price = 40
print(f"your admission cost is ${price}.")