######## Word count by input file name#####
"""def count_words(filename):
    try:
        with open(filename) as f:
            contens = f.read()
    except FileNotFoundError:
        print(f"sorry, the file {filename} does not exits.")
    else:
        letter = len(contens)
        words = contens.split()
        num_words = len(words)
        print(f"The file '{filename}' has about '{num_words}' words and '{letter}' letter.")
print("please give me file name without extention name")

a = input("please give me file name:")
b = input("please give me again file name: ")
c = input("please give me another file name: ")
aa = a + ".txt"
bb = b + ".txt"
cc = c + ".txt"
filename = [aa, bb, cc]
for filenames in filename:
    count_words(filenames)"""

###########Failing silently###########
def count_words(filename):
    try:
        with open(filename) as f:
            contens = f.read()
    except FileNotFoundError:
        pass
    else:
        letter = len(contens)
        words = contens.split()
        num_words = len(words)
        print(f"The file '{filename}' has about '{num_words}' words and '{letter}' letter.")
print("please give me file name without extention name")

a = input("please give me file name:")
b = input("please give me again file name: ")
c = input("please give me another file name: ")
aa = a + ".txt"
bb = b + ".txt"
cc = c + ".txt"
filename = [aa, bb, cc]
for filenames in filename:
    count_words(filenames)

    