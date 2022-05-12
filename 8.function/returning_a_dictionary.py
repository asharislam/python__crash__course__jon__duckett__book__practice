"""def build_person(first_name, last_name):
    person = {"first": first_name, "last":last_name}
    return person
    
musician = build_person("jimi", "hendreix")
print(musician)"""

"""def build_person(first_name, last_name, age=None):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person("jimi", "hendrix", age=27)
print(musician)"""

#using a function with a while loop

"""def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")"""


"""def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
    
while True:
    print("\nPlease tell me your name: ")
    f_name = input("please tell me your first name: ")
    l_name = input("please tell me your last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")"""

#any time take exit by "q"
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
