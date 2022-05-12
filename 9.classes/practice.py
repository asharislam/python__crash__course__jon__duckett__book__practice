class dog:
    def __init__(self, name, age):
        self.name = name.upper()
        self.age = age
    def sit(self):
        print(f"{self.name} sitting on the table.")



your_dog = dog("lucy", 3)
my_dog = dog("while", 6)
print(f"my dog name is {my_dog.name}, which age is {my_dog.age} years old.")
my_dog.sit()
your_dog.sit()
print(f"your dog name is {your_dog.name}, whih age is {your_dog.age} years old.")
