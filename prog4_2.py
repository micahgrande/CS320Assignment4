import sys
import StackMachine

print("Assignment #4-2, Micah Joseph Grande, micah.grande@gmail.com")

lines = open(sys.argv[2], 'r')
bigrig = []
for i in lines:
    token = i.split()
    bigrig = bigrig + token
stack = StackMachine.StackMachine()

for i in range(len(bigrig)):
    if bigrig[i] == "push" and bigrig [i+1].isdigit:
        stack.push(int(bigrig[i+1]))
    if bigrig[i] == "pop":
        stack.pop()
    if bigrig[i] == "add":
        stack.add()
    if bigrig[i] == "sub":
        stack.sub()
    if bigrig[i] == "mul":
        stack.mul()
    if bigrig[i] == "div":
        stack.div()
    if bigrig[i] == "mod":
        stack.mod()
