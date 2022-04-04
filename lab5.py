import random

number = [6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ["hearts", "tiles", "clovers", "pikes"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} - {self.suit}'

class Deck:
    def __init__(self):
        self.__cards = []
        for rank in number:
            for suit in suits:
                self.__cards.append(Card(rank, suit))
        random.shuffle(self.__cards)

    def shuffle(self):
        random.shuffle(self.__cards)

    def cardByNum(self, x):
        return self.__cards[x]

    def showDeck(self):
        for i in self.__cards:
            print(i)

    def popOne(self):
        tmp = self.__cards[random.randrange(0, len(self.__cards))]
        self.__cards.remove(tmp)
        return tmp

    def popSix(self):
        li = []
        for i in range(6):
            tmp = self.__cards[random.randrange(0, len(self.__cards))]
            self.__cards.remove(tmp)
            li.append(tmp)
        return li


d = Deck()
d.showDeck()

# pick a card
# print()
# print(d.cardByNum(3))

# pop a random card
# print()
# print(d.popOne())
# print()
# d.showDeck()

# pop six cards at once

# v1
# d.popSix()
# d.popSix()
# d.popSix()
# d.popSix()
# d.popSix()

# v2
print()
a = d.popSix()
for i in a:
    print(i)

print()
d.showDeck()

# to shuffle deck
# d.shuffle()
# print()
# d.showDeck()
# print()