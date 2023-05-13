

from models.animal.animal import Animal


class Dog(Animal):
    def __init__(self, chip_id: int, name: str, breed: str, size: str):
        super().__init__(chip_id, name, breed)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, str) or value not in ['small', 'medium', 'large']:
            raise TypeError("Size must be 'small', 'medium' or 'large'.")
        self.__size = value

    def get_type(self):
        return 'Dog'
