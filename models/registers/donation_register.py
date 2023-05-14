from datetime import date

from models.animal.animal import Animal
from models.person.donor import Donor


class DonationRegister():
    def __init__(self, donation_date: date, donated_animal: Animal, donor: Donor, reason: str ):
        self.__donation_date = donation_date
        self.__donated_animal = donated_animal
        self.__donor = donor
        self.__reason = reason

    @property
    def donation_date(self):
        return self.__donation_date
    
    @donation_date.setter
    def donation_date(self, value):
        self.__donation_date = value

    @property
    def donated_animal(self):
        return self.__donated_animal
    
    @donated_animal.setter
    def donated_animal(self, value):
        self.__donated_animal = value

    @property
    def donor(self):
        return self.__donor
    
    @donor.setter
    def donor(self, value):
        self.__donor = value

    @property
    def reason(self):
        return self.__reason
    
    @reason.setter
    def reason(self, value):
        self.__reason = value
