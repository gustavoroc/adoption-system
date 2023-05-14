from datetime import date

from models.animal.animal import Animal
from models.person.adopter import Adopter


class AdoptionRegister():
    def __init__(self, adoption_date: date, adopted_animal: Animal, adopter: Adopter, signed: bool ):
        self.__adoption_date = adoption_date
        self.__adopted_animal = adopted_animal
        self.__adopter = adopter
        self.__signed = signed

    @property
    def adoption_date(self):
        return self.__adoption_date
    
    @adoption_date.setter
    def adoption_date(self, value):
        self.__adoption_date = value

    @property
    def adopted_animal(self):
        return self.__adopted_animal
    
    @adopted_animal.setter
    def adopted_animal(self, value):
        self.__adopted_animal = value

    @property
    def adopter(self):
        return self.__adopter
    
    @adopter.setter
    def adopter(self, value):
        self.__adopter = value

    @property
    def signed(self):
        return self.__signed
    
    @signed.setter
    def signed(self, value):
        self.__signed = value
