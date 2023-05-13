
import datetime
from models.person.person import Person


class Adopter(Person):
    def __init__(self, cpf: str, name: str, birth_date: datetime, address: str, house_type: str, other_pets: bool):
        super().__init__(cpf, name, birth_date, address)
        self.house_type = house_type
        self.other_pets = other_pets

    @property
    def house_type(self):
        return self.__house_type

    @house_type.setter
    def house_type(self, value):
        if not isinstance(value, str) or value not in ['house', 'apartment']:
            raise TypeError("House type must be 'house' or 'apartment'.")
        self.__house_type = value

    @property
    def other_pets(self):
        return self.__other_pets

    @other_pets.setter
    def other_pets(self, value):
        if not isinstance(value, bool):
            raise TypeError("Other pets must be a boolean value.")
        self.__other_pets = value
