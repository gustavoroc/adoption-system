from datetime import date

from models.animal.animal import Animal
from models.vaccine.vaccine import Vaccine


class VaccineHistory:
    def __init__(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise ValueError('animal must be a Animal')

        self.__date_of_creation = date.today()
        self.__date_of_atualization = date.today()
        self.__animal = animal
        self.__vaccines = []

    
    @property
    def date_of_atualization(self):
        return self.__date_of_atualization
    
    @date_of_atualization.setter
    def date_of_atualization(self, value):
        self.__date_of_atualization = value

    @property
    def date_of_creation(self):
        return self.__date_of_creation
    
    @property
    def animal(self):
        return self.__animal
    
    @property
    def vaccines(self):
        return self.__vaccines
    
    def check_vaccines(self):
        vaccines = ['rabies','leptospirosis','infectious hepatitis']
        for vaccine in vaccines:
            if vaccine not in self.__vaccines:
                return False
        return True
    
    def add_vaccine(self, vaccine: Vaccine):
        if not isinstance(vaccine, Vaccine):
            raise ValueError('vaccine must be a Vaccine')
        
        self.__vaccines.append(vaccine.name)
        self.__date_of_atualization = date.today()