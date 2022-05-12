"""filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")"""

"""name_of_file = "programming.txt"

with open(name_of_file, "w") as f:
    f.write("Hello python")"""

"""filename = "programming.txt"

with open(filename, "w") as f:# without "w" this code dont be work.
    f.write("this is the python world class programming. if you like this programm then you can hire me or call me for the desition for your programming world.")
"""
    ###########191
"""path = "programming.txt"
with open(path) as f:
    content = f.read()
    print(content)

"""
#line by line read programm
"""path = "programming.txt"
with open(path) as f:
    for line in f:
        print(line)"""


#write multiple line in a .txt
"""filename = "programming.txt"
with open(filename, "w") as f:
    f.write("Name: Ashar Islam")
    f.write("\nId: 2181152018")
with open(filename) as f:
    content = f.read()
    print(content)"""

#Appending to a file
filename = "programming.txt"
with open(filename, "a") as f:
    f.write(input("please: "))
