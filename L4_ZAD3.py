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

from numpy import random, arange, mean

"""
Jako symulację wybrałyśmy sytuację polegającą na określeniu prędkości wpuszczania ludzi do auli na koncert 
w zależności od tego czy ludzie byli wpuszczani pojedynczo, czy bilety można było zakupić grupowo. 

Uczestnicy koncertu otrzymują różne atrybuty.

Symulacje przeprowadzamy w różnych wariantach: 
    -gdy można zakupić bilety tylko pojedynczo;
    -gdy można zakupić zarówno bilety grupowe, jak i pojedyncze;
    -gdy można zakupić bilety tylko grupowo. 
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
        return self.list_of_items[0]


class Participant:
    """ Participant contains participant's attributes.

    Parameters:
    _____________
    number: {int}
     number of the participant
    accompany: {int}
     how many people accompany the participant
    """
    def __init__(self, number, accompany=0):
        self.n = number
        self.acom = accompany


class Philharmonic:
    """Philharmonic includes how many doors are there to make queues.
    Parameters:
    _____________
    doors: {int}
     how many doors philharmonic has
    """
    def __init__(self, doors=1):
        self.s = doors


def list_of_probable_values(length: int):
    list_of_values = []
    #for i in range(length):
    while sum(list_of_values) < length:
        list_of_values.append(random.choice(arange(0, 5), p=[0.1, 0.4, 0.15, 0.25, 0.1]))
    list_of_values[-1] = sum(list_of_values) - length
    return list_of_values


def types_of_tickets(sold: int, types: str, list_of_values: list):
    list_of_participants = QueueBaB()
    if types == 'mixed':
        for i in range(len(list_of_values)):
            if list_of_values[i] == 0:
                list_of_participants.enqueue(Participant(number=i, accompany=list_of_values[i]))
            else:
                list_of_participants.enqueue(Participant(number=i, accompany=list_of_values[i]))
        return list_of_participants
    elif types == 'singular':
        for j in range(sold):
            list_of_participants.enqueue(Participant(number=j))
        return list_of_participants
    elif types == 'plural':
        for k in range(len(list_of_values)):
            if list_of_values[k] == 0:
                list_of_participants.enqueue(Participant(number=k, accompany=list_of_values[k]+1))
                k += Participant(number=k).acom
            else:
                list_of_participants.enqueue(Participant(number=k, accompany=list_of_values[k]))
                k += Participant(number=k).acom
        return list_of_participants


def simulation_queue(people: int, doors: int, types: str, list_of_tickets: list):
    philharmonic = Philharmonic()
    philharmonic.s = doors
    participants = types_of_tickets(people, types, list_of_tickets)
    list_of_queues = []
    times = []
    time_tickets = 2
    time_go_in = 1
    for j in range(doors):
        list_of_queues.append(QueueBaB())
        times.append([])
    while not participants.is_empty():
        for queue in list_of_queues:
            if not participants.is_empty():
                queue.enqueue(int(participants.first().acom))
                participants.dequeue()
    for i in range(len(list_of_queues)):
        while not list_of_queues[i].is_empty():
            if list_of_queues[i].first() == 0:
                times[i].append(time_tickets + time_go_in)
                list_of_queues[i].dequeue()
            else:
                times[i].append((int((list_of_queues[i].first() / 2) + 1*list_of_queues[i].first())))
                list_of_queues[i].dequeue()
    whole_times = []
    for n in range(len(times)):
        whole_times.append(sum(times[n]))
    whole_times.sort()
    return whole_times[-1]


def simulation(n_simulations, n_people, n_doors):
    singular_time = []
    plural_time = []
    mixed_time = []
    for _ in range(n_simulations):
        a = list_of_probable_values(n_people)
        singular_time.append(simulation_queue(n_people, n_doors, 'singular', a))
        plural_time.append(simulation_queue(n_people, n_doors, 'plural', a))
        mixed_time.append(simulation_queue(n_people, n_doors, 'mixed', a))
    print(mean(singular_time))
    print(mean(plural_time))
    print(mean(mixed_time))

simulation(500, 20, 1)
print('_____________')
simulation(500, 20, 2)
print('_____________')
simulation(500, 20, 4)
print('_____________')

a = list_of_probable_values(20)
print(simulation_queue(20, 4, 'singular', a))
print(simulation_queue(20, 4, 'mixed', a))
print(simulation_queue(20, 4, 'plural', a))
print('_____________')
simulation_queue_list_4 = []

print(simulation_queue(20, 2, 'singular', a))
print(simulation_queue(20, 2, 'mixed', a))
print(simulation_queue(20, 2, 'plural', a))
print('_____________')
print(simulation_queue(20, 1, 'singular', a))
print(simulation_queue(20, 1, 'mixed', a))
print(simulation_queue(20, 1, 'plural', a))


