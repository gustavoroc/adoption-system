from abc import ABC
from datetime import datetime

class Person(ABC):
    def __init__(self, cpf: str, name: str, birth_date: datetime, address: str):
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date
        self.address = address

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        if not isinstance(value, str):
            raise TypeError("CPF must be a string.")
        self.__cpf = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self.__name = value

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        if not isinstance(value, datetime):
            raise TypeError("Birth date must be a datetime object.")
        self.__birth_date = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("Address must be a string.")
        self.__address = value
