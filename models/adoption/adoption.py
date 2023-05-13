import datetime

from models.animal.animal import Animal
from models.person.adopter import Adopter


class Adoption:
    def __init__(self, date: datetime, animal: Animal, adopter: Adopter, signed_term: bool):
        self.date = date
        self.animal = animal
        self.adopter = adopter
        self.signed_term = signed_term

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if not isinstance(value, datetime):
            raise TypeError("Date must be a datetime object.")
        self.__date = value

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, value):
        if not isinstance(value, Animal):
            raise TypeError("Animal must be an instance of Animal class.")
        self.__animal = value

    @property
    def adopter(self):
        return self.__adopter

    @adopter.setter
    def adopter(self, value):
        if not isinstance(value, Adopter):
            raise TypeError("Adopter must be an instance of Adopter class.")
        self.__adopter = value

    @property
    def signed_term(self):
        return self.__signed_term

    @signed_term.setter
    def signed_term(self, value):
        if not isinstance(value, bool):
            raise TypeError("Signed term must be a boolean value.")
        self.__signed_term = value
