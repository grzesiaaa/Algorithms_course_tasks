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

def matches(op, cl):
    opens = "<"
    closers = ">"
    return opens.index(op) == closers.index(cl)


def checking_HTML_correctness(filename):
    """
    Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
    Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
    Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
    """
    s = Stack()
    balanced = True
    index = 0

    file_obj = open(filename, 'r')
    text = file_obj.read()


print(checking_HTML_correctness("L4_ZAD4_sampleHTML_1.txt"))