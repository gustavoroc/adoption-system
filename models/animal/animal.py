from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, chip_id: int, name: str, breed: str):
        self.chip_id = chip_id
        self.name = name
        self.breed = breed

    @property
    def chip_id(self):
        return self.__chip_id

    @chip_id.setter
    def chip_id(self, value):
        if not isinstance(value, int):
            raise TypeError("Chip ID must be an integer.")
        self.__chip_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self.__name = value

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, value):
        if not isinstance(value, str):
            raise TypeError("Breed must be a string.")
        self.__breed = value

    @abstractmethod
    def get_type(self):
        pass