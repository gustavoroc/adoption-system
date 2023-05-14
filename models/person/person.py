from abc import ABC, abstractmethod
from datetime import date


class Person(ABC):  # Person é uma classe abstrata
    def __init__(self, cpf: str, name: str, birth_date: date, address: str):
        if not isinstance(birth_date, date):
            raise TypeError("birth_date must be a date object")
        
        self.__cpf = cpf
        self.__name = name
        self.__birth_date = birth_date
        self.__address = address

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        self.__birth_date = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def check_adult(self):
        current_date = date.today()
        age = current_date.year - self.birth_date.year

        if age > 18:
            return True
        elif age == 18:
            if (self.birth_date.month, self.birth_date.day) <= (current_date.month, current_date.day):
                return True

        return False
    
    def __str__(self) -> str:
        return f"Nome: {self.name}\nCPF: {self.cpf}\nData de nascimento: {self.birth_date}\nEndereço: {self.address}\n"

    @abstractmethod
    def role(self):
        pass