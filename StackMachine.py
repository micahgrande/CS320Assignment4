class StackMachine:
    def __init__(self):
        self.__data = []
    def Push(self, x):
        self.__data.append(x)
    def Pop(self):
        return self.__data.pop()
    def add(self):
        if len(self.__data) > 1:
            self.append(self.pop() + self.pop())
    def sub(self):
        if len(self.__data) > 1:
            self.append(self.pop() - self.pop())
    def mul(self):
        if len(self.__data) > 1:
            self.append(self.pop() * self.pop())
    def div(self):
        if len(self.__data) > 1:
            self.append(self.pop() / self.pop())
    def mod(self):
        if len(self.__data) > 1:
            self.append(self.pop() % self.pop())