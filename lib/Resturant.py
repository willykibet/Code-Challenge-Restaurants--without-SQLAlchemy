from lib.review import *

class Customer:
    _all = []

    def __init__(self, name):
        #the airline that's being initialized add an airline to _all[]
        Customer._all.append(self)
        self._name = name

    @property
    def name(self):
        return self._name
    # name = property(name)

    @name.setter
    def name(self, name):
        self._name = name

    def add_review(restaurant, content):
        Review(restaurant, self, content)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_all_by_name(cls, name):
        return [customer for customer in cls.all() if customer.name == name]

    @classmethod
    def find_by_name(cls, name):
        return [customer for customer in cls.all() if customer.name == name][0]
xs