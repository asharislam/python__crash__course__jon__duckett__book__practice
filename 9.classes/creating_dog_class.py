#158
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog("While", 6)

"""print(f"My dog's name is {my_dog.name}. whose age is {my_dog.age}")"""

#calling methods
my_dog.sit()
my_dog.roll_over()

#creating multiple instances
my_dog = Dog("while", 6)
your_dog = Dog("Lucy", 3)

print(f"My dog's name is {my_dog.name.title()} and which age is {my_dog.age} years old.")
print(f"Your dog is {your_dog.name.title()} and which age is {your_dog.age} years old.")



