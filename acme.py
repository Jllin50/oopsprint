import random


class Product():
    def __init__(self, name, price=10, weight=20, flammability=float(.5),
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < .5:
            return 'Not so stealable...'
        elif ((ratio >= .5) & (ratio < 1)):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        ratio = self.flammability * self.weight
        if ratio < 10:
            return '...fizzle.'
        elif ((ratio >= 10) & (ratio < 50)):
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    def __init__(self, name, price, flammability, identifier, weight=10):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif ((self.weight >= 5) & (self.weight < 15)):
            return 'Hey that hurt!'
        else:
            return 'OUCH!'