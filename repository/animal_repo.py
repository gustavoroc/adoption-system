import pickle
from typing import List, Optional
from errors.client_error import ClientError
from models.animal.animal import Animal

class AnimalRepository:
    def __init__(self):
        self.__filename = "animals.pkl"
        self.__animals: List[Animal] = []

    def __load_data(self):
        try:
            with open(self.__filename, "rb") as f:
                self.__animals: List[Animal] = pickle.load(f)
        except FileNotFoundError:
            self.__animals: List[Animal] = []

    def save_to_file(self):
        with open(self.__filename, "wb") as f:
            pickle.dump(self.__animals, f)

    def create_animal(self, animal: Animal) -> None:
        self.__load_data()
        if not isinstance(animal, Animal):
            raise ClientError("Input must be an instance of Animal class.")
        for existing_animal in self.__animals:
            if existing_animal.chip_number == animal.chip_number:
                raise ClientError("An animal with the same chip number already exists.")
        self.__animals.append(animal)
        self.save_to_file()

    def get_all_animals(self) -> List[Animal]:
        self.__load_data()
        return self.__animals

    def get_available_animals(self) -> List[Animal]:
        self.__load_data()
        available_animals = []
        for animal in self.__animals:
            if not animal.isAdopted:
                available_animals.append(animal)
        return available_animals
                
    def get_animal_by_chip(self, chip_number: str) -> Optional[Animal]:
        self.__load_data()
        if not isinstance(chip_number, str):
            raise ClientError("Chip number must be a string.")
        for animal in self.__animals:
            if animal.chip_number == chip_number:
                return animal
        raise ClientError("No animal with the provided chip number exists.")

    def update_animal(self, chip_number: str, new_animal: Animal) -> Optional[Animal]:
        self.__load_data()
        if not isinstance(chip_number, str) or not isinstance(new_animal, Animal):
            raise ClientError("Chip number must be a string and new_animal must be an instance of Animal class.")
        for i, animal in enumerate(self.__animals):
            if animal.chip_number == chip_number:
                self.__animals[i] = new_animal
                self.save_to_file()
                return new_animal
        raise ClientError("No animal with the provided chip number exists.")

    def delete_animal(self, chip_number: str) -> bool:
        self.__load_data()
        if not isinstance(chip_number, str):
            raise ClientError("Chip number must be a string.")
        for i, animal in enumerate(self.__animals):
            if animal.chip_number == chip_number:
                del self.__animals[i]
                self.save_to_file()
                return True
        raise ClientError("No animal with the provided chip number exists.")
