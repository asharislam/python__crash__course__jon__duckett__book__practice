"""with open("pi_digit.txt") as f:
    content = f.read()
print(content)"""

"""with open("pi_digit.txt") as f:
    for line in f:
        print(line)"""

"""with open("pi_digit.txt") as f:
    content = f.read()
print(content)
"""
"""with open("pi_digit.txt") as f:
    content = f.read()
print(content.rstrip())#here strip are not clear"""

#file paths # for path you must use Slash(/) othewise double BackSlash()
file_path = "F:/WORKING/Programming/python/python_crash_course/files_and_exceptions.py/text_file/test.txt"
with open(file_path) as f:
    content = f.read()
    print(content)

"""######---If you try to use backslashes in a file path, you’ll get an error because the backslash is
used to escape characters in strings. For example, in the path "C:\path\to\file.txt",
the sequence \t is interpreted as a tab. If you need to use backslashes, you can escape
each one in the path, like this: "C:\\path\\to\\file.txt".---"""


