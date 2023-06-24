from abc import ABC, abstractmethod
from errors.client_error import ClientError
from models.vaccine.vaccine_history import VaccineHistory

class Animal(ABC):
    def __init__(self, chip_number: str, name: str, breed: str):
        self.__chip_number = chip_number
        self.__name = name
        self.__breed = breed
        self.__isAdopted = False
        self.__vaccine_history = VaccineHistory(self)

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, value):
        self.__chip_number = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, value):
        self.__breed = value

    @property
    def vaccine_history(self):
        return self.__vaccine_history
    
    @property
    def isAdopted(self):
        return self.__isAdopted
    
    @isAdopted.setter
    def isAdopted(self, value):
        if not isinstance(value, bool):
            raise ClientError('isAdopted must be a boolean value')

        self.__isAdopted = value
        
    def animal_type(self):
        return 'Animal'
    