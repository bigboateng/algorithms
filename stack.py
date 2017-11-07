class Stack:
    def __init__(self):
        self.s = []

    def push(self, o):
        self.s.append(o)

    def pop(self):
        return self.s.pop()

    def peek(self):
        return self.s[-1]

    def isEmpty(self):
        return len(self.s) is 0

    def __repr__(self):
        return str(self.s)


def parenthesis():   
    In = "(()())"
    balanced = True
    i = 0
    s = Stack()
    while i is not len(In) and balanced:
        if In[i] == "(":
            s.push("(")
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        i += 1
    print(balanced)

def paranthesisGeneral():
    s = Stack()
    opened = "({["
    closed = ")}]"
    In = "[(){}()]]"
    i = 0
    balanced = True
    while not i == len(In) and balanced:
        bracket = In[i]
        if bracket in opened:
            s.push(bracket)
        else:
            if s.isEmpty():
                balanced = False
            else:
                if opened.index(s.peek()) == closed.index(bracket):
                    s.pop()
                else:
                    balanced = False
        i += 1
    print(balanced)

paranthesisGeneral()







    
