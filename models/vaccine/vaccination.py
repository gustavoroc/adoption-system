import datetime

from models.animal.animal import Animal


class Vaccination:
    def __init__(self, date: datetime, animal: Animal, vaccine: str):
        self.date = date
        self.animal = animal
        self.vaccine = vaccine

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
    def vaccine(self):
        return self.__vaccine

    @vaccine.setter
    def vaccine(self, value):
        if not isinstance(value, str):
            raise TypeError("Vaccine must be a string.")
        self.__vaccine = value
