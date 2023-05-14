from datetime import date
from models.person.person import Person


class Adopter(Person):  # Adopter herda de Person
    def __init__(self, cpf: str, name: str, birth_date: date, address: str, home_type: str, has_other_pets: bool):
        super().__init__(cpf, name, birth_date, address)
        self.__home_type = home_type
        self.__has_other_pets = has_other_pets

    @property
    def home_type(self):
        return self.__home_type

    @home_type.setter
    def home_type(self, value):
        self.__home_type = value

    @property
    def has_other_pets(self):
        return self.__has_other_pets

    @has_other_pets.setter
    def has_other_pets(self, value):
        self.__has_other_pets = value

    def role(self):
        return "Adotante"