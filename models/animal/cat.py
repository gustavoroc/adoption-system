from models.animal.animal import Animal


class Cat(Animal):
    def __init__(self, chip_number: str, name: str, breed: str):
        super().__init__(chip_number, name, breed)
        self.__size = 'small'

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
    
    def animal_type(self):
        return "Cat"