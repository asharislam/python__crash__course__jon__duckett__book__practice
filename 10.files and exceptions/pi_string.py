#working with a file content

filename = "pi_digit.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()#working but not understand . page 188

    print(pi_string)
    
    
    #large_files_one_million_digit
file_name = "pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    print(f"{pi_string[:52]}...")
    print(len(pi_string))
