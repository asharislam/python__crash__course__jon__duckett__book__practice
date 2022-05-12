"""path = "F:\\WORKING\\Programming\\python\\python_crash_course\\10.files and exceptions\\test.txt"

with open(path) as f:
    for line in f:
        print(line)
"""
#strip
file_name = "pi_digit.txt"
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip()) # rstrip for remove space

