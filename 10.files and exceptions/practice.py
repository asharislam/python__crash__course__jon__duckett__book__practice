pathline = "practice.txt"
with open(pathline, "w") as f:
    content = input("For print on the txt then please say samething: ")
    f.write(content)
with open(pathline) as f:
    content = f.read()
print(content)