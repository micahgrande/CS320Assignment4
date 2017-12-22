import sys

print("Assignment #4-1, Micah Joseph Grande, micah.grande@gmail.com")

file = open(sys.argv[-1], 'r')
line = file.readlines()

for i in line:
    token = i.split()
    print(', '.join(token))