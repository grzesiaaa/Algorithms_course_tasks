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
    with open(filename, 'r') as f:
        html_code = f.read()
    s = Stack()
    balanced = True
    index = 0
    list_of_tags_index = []
    while index < len(html_code) and balanced:
        # symbol is a one char of code
        symbol = html_code[index]
        # when we found char "<" we added it on stack and append index on a special
        # list of indexes of html tags
        # everything is okay because every html code begin with <
        if symbol == "<":
            s.push(symbol)
            list_of_tags_index.append([index])
        else:
            # we end if stack is empty
            if s.isEmpty():
                balanced = False
            # if we foun "/" there are two options
            elif len(html_code) - 3 > index:
                if html_code[index - 1] + symbol + html_code[index + 1] == "<!-":
                    j = 0
                    while html_code[index + j:index + j + 3] != "-->":
                        j += 1
                    index += j + 2
                    list_of_tags_index.pop()
            if symbol in "/":
                # we check that list is longer of one index to
                # don't get error
                if len(html_code) == index + 1:
                    balanced = False
                else:
                    # if we found a tag "/>"" that mean that on stack should be "<"
                    if html_code[index + 1] in ">":
                        # so we poping stack, end deleting index from list of index
                        # because we want only indexes of tags type <></>
                        s.pop()
                        list_of_tags_index.pop()
                        index += 1
                        # if there is "</" that mean that it's an opening of closing tag
                    elif html_code[index - 1] in "<":
                        s.push(symbol)
            elif symbol in ">":
                # if top is "/" that means that on stack should be <></>
                top = s.pop()
                if top in '/':
                    list_of_tags_index[-1].append(index)
                    # if its <></> so size of stack should be minumum 3
                    if s.size() < 3:
                        balanced = False
                    # we poping three elements
                    else:
                        s.pop()
                        s.pop()
                        s.pop()
                else:
                    # in other way we adding our top and sumbol on stack and append index to list of
                    # indexes
                    s.push(top)
                    s.push(symbol)
                    list_of_tags_index[-1].append(index)
        index = index + 1
    # now we check correctnes that attributes in tags are same np. <a></a>
    html_attributes = []
    # print(html_code[212:])
    for i in list_of_tags_index:
        #print(i)
        # we are selecting the first word inside each html tag from index_lists
        x = html_code[i[0]:i[1]].split()[0]
        # we want attribute without / on the begining
        if x[1] in '/':
            html_attributes.append(x[2:])
        # we want also attribute without < on the beginning
        else:
            html_attributes.append(x[1:])
    # we take index = 1 because we push first elementof list on stack
    index = 1
    s.push(html_attributes[0])
    while index < len(html_attributes):
        # we will check that the next attribute is the same as our from stack
        symbol = html_attributes[index]
        dropped = s.pop()
        if symbol != dropped:
            # if no lets push them on stack
            s.push(dropped)
            s.push(symbol)
        index = index + 1
    # if stack is empty and there was no problem return True
    if balanced and s.isEmpty():
        return True
    else:
        return False


print(checking_HTML_correctness("L4_ZAD4_sampleHTML_1.txt"))