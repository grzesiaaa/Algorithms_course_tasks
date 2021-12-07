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
    def __init__(self, number, place="out", accompany=0):
        self.n = number
        self.p = place
        self.acom = accompany

    def get_inside(self):
        """Changes place of the participant when gets inside the philharmonic"""
        self.p = "in"


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


def list_of_normal_dis_values(lenght, n, m):
    list_of_values = []
    for i in range(lenght):
        list_of_values.append(normal_dis_value(n, m))
    return list_of_values


def types_of_tickets(sold, types, list_of_tickets):
    list_of_participants = QueueBaB()
    list_of_values = list_of_tickets
    if types == 'mixed':
        for i in range(sold):
            list_of_participants.enqueue(Participant(number=i, accompany=list_of_values[i]))
            if Participant(number=i).acom == 0:
                i += 1
            else:
                i += 1 + Participant(number=i).acom
        return list_of_participants
    elif types == 'singular':
        for i in range(sold):
            list_of_participants.enqueue(Participant(number=i))
        return list_of_participants
    """elif types == 'plural':
        for i in range(sold):
            a = normal_dis_value(n, m)
            if a == 0:
                
            else:
                list_of_participants.enqueue(Participant(number=i, accompany=a))"""


def symulation_queue(people: int, doors: int, types: str, list_of_tickets: list):
    philharmonic = Philharmonic()
    philharmonic.s = doors
    participants = types_of_tickets(people, types, list_of_tickets)
    list_of_queues = []
    times = []
    time_tickets = 2
    time_go_in = 1
    for j in range(doors):
        list_of_queues.append(QueueBaB())
        times.append([0])
    while not participants.is_empty():
        for queue in list_of_queues:
            queue.enqueue(int(participants.first().acom))
            participants.dequeue()
    for i in range(len(list_of_queues)):
        while not list_of_queues[i].is_empty():
            if list_of_queues[i].first() == 0:
                times[i].append(time_tickets + time_go_in)
                list_of_queues[i].dequeue()
            else:
                times[i].append((int((list_of_queues[i].first() / 2 + 1) * 2)))
                list_of_queues[i].dequeue()
    whole_times = []
    for n in range(len(times)):
        whole_times.append(sum(times[n]))
    whole_times.sort()
    return whole_times[-1]


a = list_of_normal_dis_values(20, 2, 1)
print(symulation_queue(20, 4, 'singular', a))
print(symulation_queue(20, 4, 'mixed', a))
print(symulation_queue(20, 2, 'mixed', a))
print(symulation_queue(20, 1, 'singular', a))
print(symulation_queue(20, 1, 'mixed', a))


