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

import random

"""
Jako symulację wybrałyśmy sytuację polegającą na określeniu prędkości wpuszczania ludzi do auli na koncert 
w zależności od tego czy ludzie byli wpuszczani pojedynczo, czy bilety można było zakupić grupowo. 

Uczestnicy koncertu otrzymują różne atrybuty.

Symulacje przeprowadzamy w różnych wariantach: 
    -gdy można zakupić bilety tylko pojedynczo;
    -gdy można zakupić zarówno bilety grupowe, jak i pojedyncze;
    -gdy pojawiają się tzw. uczestnicy VIP, którzy mogą wejść bez kolejki. 

"""


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
        self.hap = happiness
        self.acom = accompany

    def get_inside(self):
        """Changes place of the participant when gets inside the philharmonic"""
        self.p = "in"

    def get_angry(self):
        self.hap -= 10


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


def types_of_tickets(sold):
    list_of_participants = []
    for i in range(sold):
        list_of_participants.append(Participant(number=i))
        if Participant(number=i).acom == 0:
            i += 1
        else:
            i += 1 + Participant(number=i).acom
    return list_of_participants


def
