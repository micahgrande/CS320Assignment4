import sys

print("Assignment #4-1, Micah Joseph Grande, micah.grande@gmail.com")
name = sys.argv[-1]
file = open(name, 'r')
line = file.readLines()

for i in line:
    token = i.split()
    print(', '.join(token))