"""f = open("pi_digits.txt", "r")
print(f.name)
print(f.mode)
f.close()"""
####################
with open('test.txt') as f:
    for line in f:
        print(line)
    
    """f_contents = f.readlines()
    print(f_contents, end='')

    f_contents = f.readlines()
    print(f_contents, end='')
"""
