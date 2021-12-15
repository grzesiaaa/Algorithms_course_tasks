class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def move_disk(init, final, temp, amount):
    if amount == 0:
        return "Nothing to move"
    elif amount == 1:
        final[0].push(init[0].pop())
        print("moving disk from", init[1], "to", final[1])
        return final[0]
    else:
        move_disk(init, temp, final, amount-1)
        print("moving disk from", init[1], "to", final[1])
        final[0].push(init[0].pop())
        move_disk(temp, final, init, amount-1) #???/
        return final[0]

def Hanoi(amount):
    A = [Stack(), "A"]
    B = [Stack(), "B"]
    C = [Stack(), "C"]
    for i in range(1,amount+1):
        A[0].push(i)
    return move_disk(A,B,C, amount)

print(Hanoi(4))