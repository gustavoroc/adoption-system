from models.vaccine.vaccine_history import VaccineHistory

class Animal:
    def __init__(self, chip_number: str, name: str, breed: str, size: str):
        self.__chip_number = chip_number
        self.__name = name
        self.__breed = breed
        self.__size = size
        self.__isAdopted = False
        self.__vaccine_history = VaccineHistory()

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
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def vaccine_history(self):
        return self.__vaccine_history
    
    @property
    def isAdopted(self):
        return self.__isAdopted
    
    @isAdopted.setter
    def isAdopted(self, value):
        if not isinstance(value, bool):
            raise ValueError('isAdopted must be a boolean value')

        self.__isAdopted = value
    