import sys

print("Assignment #4-1, Micah Joseph Grande, micah.grande@gmail.com")

file = open(sys.argv[2], 'r')
line = file.readLines()

for i in line:
    token = i.split()
    print(', '.join(token))