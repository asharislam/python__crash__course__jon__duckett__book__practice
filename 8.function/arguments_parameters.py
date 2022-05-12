#positional arguments

"""def describe_pet (animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "harry")
"""
#keyword arguments
#133
"""def descrive_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
descrive_pet(animal_type="hamster", pet_name="harry")
descrive_pet(pet_name= "harry", animal_type="hamster")"""

##default_values

"""def describe_pet(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name= "willie")"""

#avoiding argument errors

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet("dog", "tommy")





