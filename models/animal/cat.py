from models.animal.animal import Animal


class Cat(Animal):
    def __init__(self, chip_number: str, name: str, breed: str):
        super().__init__(chip_number, name, breed)
    
    def animal_type():
        return "Gato"