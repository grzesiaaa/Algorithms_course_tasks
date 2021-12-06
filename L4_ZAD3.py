"""
Rozważ sytuację z życia wziętą, np.: 
- auta w kolejce do myjni,
- kasy w supermarkecie,
- samoloty na pasie startowym, 
- okienko w banku. 
Postaw pytanie badawcze. Wykorzystując liniowe struktury danych 
zaprojektuj i przeprowadź symulację, która udzieli na nie odpowiedzi. 
Pamiętaj o określeniu wszystkich uproszczeń swojego modelu. 
"""

from numpy import random

"""
Jako symulację wybrałyśmy sytuację polegającą na określeniu prędkości wpuszczania ludzi do auli na koncert 
w zależności od tego czy ludzie byli wpuszczani pojedynczo, czy bilety można było zakupić grupowo. 

Uczestnicy koncertu otrzymują różne atrybuty.

Symulacje przeprowadzamy w różnych wariantach: 
    -gdy można zakupić bilety tylko pojedynczo;
    -gdy można zakupić zarówno bilety grupowe, jak i pojedyncze;
    -gdy pojawiają się tzw. uczestnicy VIP, którzy mogą wejść bez kolejki. 

"""


class QueueBaB(object):
    """
    Klasa implementująca kolejkę za pomocą pythonowej listy tak,
    że początek kolejki jest przechowywany na początku listy.
    """

    def __init__(self):
        self.list_of_items = []

    def enqueue(self, item):
        """
        Metoda służąca do dodawania obiektu do kolejki.
        Pobiera jako argument obiekt który ma być dodany.
        Niczego nie zwraca.
        """
        self.list_of_items.insert(len(self.list_of_items), item)

    def dequeue(self):
        """
        Metoda służąca do ściągania obiektu do kolejki.
        Nie pobiera argumentów.
        Zwraca ściągnięty obiekt.
        """
        return self.list_of_items.pop(0)

    def is_empty(self):
        """
        Metoda służąca do sprawdzania, czy kolejka jest pusta.
        Nie pobiera argumentów.
        Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
        """
        return self.list_of_items == []

    def size(self):
        """
        Metoda służąca do określania wielkości kolejki.
        Nie pobiera argumentów.
        Zwraca liczbę obiektów w kolejce.
        """
        return len(self.list_of_items)

    def __str__(self):
        return str(self.list_of_items)

    def first(self):
        return self.list_of_items[0] #na potrzeby zadania 3


class Participant:
    """ Participant contains participant's attributes.

    Parameters:
    _____________
    number: {int}
     number of the participant
    place: {str}
     place of participant, in or outside the philharmonic
    happiness: {int}
     amount of happiness of the participant; goes down when sees VIPParticipant
    accompany: {int}
     how many people accompany the participant
    """
    def __init__(self, number, place="out", happiness=100, accompany=0):
        self.n = number
        self.p = place
        "self.hap = happiness"
        self.acom = accompany

    def get_inside(self):
        """Changes place of the participant when gets inside the philharmonic"""
        self.p = "in"

    """def get_angry(self):
        self.hap -= 10"""


class VIPParticipant:
    def __init__(self, place="out"):
        self.p = place


class Philharmonic:
    """Philharmonic includes how many doors are there to make queues.
    Parameters:
    _____________
    doors: {int}
     how many doors philharmonic has
    """
    def __init__(self, doors=1):
        self.s = doors


def normal_dis_value(n, m):
    return int(random.normal(n, m))


def types_of_tickets(sold):
    list_of_participants = QueueBaB()
    for i in range(sold):
        list_of_participants.enqueue(Participant(number=i, accompany=normal_dis_value(2, 1)))
        if Participant(number=i).acom == 0:
            i += 1
        else:
            i += 1 + Participant(number=i).acom
    return list_of_participants


def symulation_queue(people: int, doors: int):
    philharmonic = Philharmonic()
    philharmonic.s = doors
    participants = types_of_tickets(people)
    list_of_queues = []
    times = []
    time_tickets = 2
    time_go_in = 1
    for j in range(doors):
        list_of_queues.append(QueueBaB())
        times.append(0)
    while not participants.is_empty():
        for queue in list_of_queues:
            queue.enqueue(participants.first())
            participants.dequeue()
    for i, queue in set(list_of_queues):
        while not queue.is_empty():
            if queue.first().acom == 0:
                times[i] += time_tickets + time_go_in
                queue.dequeue()
            else:
                times[i] += (int(participants.first().acom) / 2 + 1) * 2
                queue.dequeue()
    return times.sort()


print(symulation_queue(20, 2))
