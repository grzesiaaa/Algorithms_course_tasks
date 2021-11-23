class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Sprawdź czy lista jest pusta.
        """
        return self.head == None

    def add(self, item):
        """
        Dodaj element na początek listy.
        """
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """
        Zwróć dlugość listy.
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        """
        Sprawdź czy element jest w liście.
        """
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        """
        Usuń podany element z listy.
        """
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __str__(self):
        """
        Wypisz listę na ekran.
        """
        current = self.head
        li = []
        while current != None:
            li.append(current.get_data())
            current = current.get_next()
        s = ("elements in the list are [" + ', '.join(['{}'] * len(li)) + "]")
        return s.format(*li)

    def append(self, item):
        """
        Metoda dodająca element na koniec listy.
        Przyjmuje jako argument obiekt, który ma zostać dodany.
        Niczego nie zwraca.
        """
        current = self.head
        temp = Node(item)
        previous = None

        if self.is_empty():
            self.add(item)
        else:
            while current != None:
                previous = current
                current = current.get_next()
            previous.set_next(temp)

    def index(self, item):
        """
        Metoda podaje miejsce na liście,
        na którym znajduje się określony element -
        element pod self.head ma indeks 0.
        Przyjmuje jako argument element,
        którego pozycja ma zostać określona.
        Zwraca pozycję elementu na liście lub None w przypadku,
        gdy wskazanego elementu na liście nie ma.
        """
        current = self.head
        found = False
        index = 0

        while current != None and not found:
            if current.get_data() != item:
                index += 1
                current = current.get_next()
            else:
                found = True

        if found:
            return index
        else:
            return None

    def insert(self, pos, item):
        """
        Metoda umieszcza na wskazanej pozycji zadany element.
        Przyjmuje jako argumenty pozycję,
        na której ma umiescić element oraz ten element.
        Niczego nie zwraca.
        Rzuca wyjątkiem IndexError w przypadku,
        gdy nie jest możliwe umieszczenie elementu
        na zadanej pozycji (np. na 5. miejsce w 3-elementowej liście).
        """
        current = self.head
        previous = None
        index = 0
        temp = Node(item)

        if pos > self.size() or pos < -self.size()-1:
            raise IndexError("Incorrect position")

        elif pos == 0:
            temp.set_next(self.head)
            self.head = temp

        else:
            if pos < 0:
                pos = pos + self.size() + 1

            while current != None and index < pos:
                previous = current
                current = current.get_next()
                index += 1

            previous.set_next(temp)
            temp.set_next(current)

    def pop(self, pos=-1):
        """
        Metoda usuwa z listy element na zadaniej pozycji.
        Przyjmuje jako opcjonalny argument pozycję,
        z której ma zostać usunięty element.
        Jeśli pozycja nie zostanie podana,
        metoda usuwa (odłącza) ostatni element z listy.
        Zwraca wartość usuniętego elementu.
        Rzuca wyjątkiem IndexError w przypadku,
        gdy usunięcie elementu z danej pozycji jest niemożliwe.
        """

        current = self.head
        previous = None
        index = 0

        if self.is_empty():
            raise IndexError("Nothing to pop")
        elif pos >= self.size() or pos < -self.size():
            raise IndexError("Incorrect position")

        elif self.size() == 1:
            self.head = None
            return current.get_data()

        else:
            if pos < 0:
                pos = pos + self.size()

            while current != None and index < pos:
                previous = current
                current = current.get_next()
                index += 1

            if previous is None:
                self.head = current.get_next()
                return current.get_data()
            else:
                previous.set_next(current.get_next())
                return current.get_data()

    def peek(self):
        """
        Metoda podaje wartość elementu na końcu listy.
        Nie pobiera argumentów.
        Jeśli lista jest pusta, rzuca wyjątkiem IndexError.
        """
        current = self.head
        previous = None

        if self.is_empty():
            raise IndexError("Object is empty")

        while current != None:
            previous = current
            current = current.get_next()
        return previous.get_data()

