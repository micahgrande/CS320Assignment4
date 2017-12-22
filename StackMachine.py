class StackMachine:
    def __init__(self):
        self.__data = []
    def push(self, x):
        self.__data.append(x)
    def pop(self):
        return self.__data.pop()
    def add(self):
        if len(self.__data) > 1:
            self.__data.append(self.__data.pop() + self.__data.pop())
    def sub(self):
        if len(self.__data) > 1:
            self.__data.append(self.__data.pop() - self.__data.pop())
    def mul(self):
        if len(self.__data) > 1:
            self.__data.append(self.__data.pop() * self.__data.pop())
    def div(self):
        if len(self.__data) > 1:
            self.__data.append(self.__data.pop() / self.__data.pop())
    def mod(self):
        if len(self.__data) > 1:
            self.__data.append(self.__data.pop() % self.__data.pop())