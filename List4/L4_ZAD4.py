import re

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

def checking_HTML_correctness(filename):
    """
    Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
    Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
    Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
    """
    with open(filename, 'r') as f:
        html_code = f.read()

    html_code = list(re.sub("(<!--.*?-->)", "", html_code))

    all_tags_list = []
    tags_stack = Stack()

    no_closing_tags = ["!DOCTYPE", "br", "meta", "link", "img", "col",
                       "command", "hr", "input", "col", "base", "area", ]

    for index in range(len(html_code)):
        symbol = html_code[index]
        if symbol == "<":
            start = index
        if symbol == ">":
            string = ""
            end = index
            for i in range(start + 1, end):
                string += str(html_code[i])
            all_tags_list.append(string.split(" ")[0])

    good_tag_list =[]
    for tag in all_tags_list:
        if tag in no_closing_tags:
            pass
        else:
            good_tag_list.append(tag)

    for i in range(0, len(good_tag_list)):
        if tags_stack.isEmpty():
            tags_stack.push(good_tag_list[i])
        else:
            if good_tag_list[i] == "/" + tags_stack.peek():
                tags_stack.pop()
            else:
                tags_stack.push(good_tag_list[i])

    if tags_stack.isEmpty():
        return True
    else:
        return False
