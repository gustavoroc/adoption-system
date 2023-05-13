import datetime

from models.animal.animal import Animal
from models.person.donor import Donor


class Donation:
    def __init__(self, date: datetime, animal: Animal, donor: Donor, reason: str):
        self.date = date
        self.animal = animal
        self.donor = donor
        self.reason = reason

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
    def donor(self):
        return self.__donor

    @donor.setter
    def donor(self, value):
        if not isinstance(value, Donor):
            raise TypeError("Donor must be an instance of Donor class.")
        self.__donor = value

    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, value):
        if not isinstance(value, str):
            raise TypeError("Reason must be a string.")
        self.__reason = value
