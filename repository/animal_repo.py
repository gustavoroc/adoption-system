import pickle
from typing import List, Optional
from models.animal.animal import Animal

class AnimalRepository:
    def __init__(self):
        self.__filename = "animals.pkl"
        try:
            with open(self.__filename, "rb") as f:
                self.__animals: List[Animal] = pickle.load(f)
        except FileNotFoundError:
            self.__animals: List[Animal] = []

    def save_to_file(self):
        with open(self.__filename, "wb") as f:
            pickle.dump(self.__animals, f)

    def create_animal(self, animal: Animal) -> None:
        if not isinstance(animal, Animal):
            raise ValueError("Input must be an instance of Animal class.")
        for existing_animal in self.__animals:
            if existing_animal.chip_number == animal.chip_number:
                raise ValueError("An animal with the same chip number already exists.")
        self.__animals.append(animal)
        self.save_to_file()

    def get_all_animals(self) -> List[Animal]:
        return self.__animals

    def get_available_animals(self) -> List[Animal]:
        available_animals = []
        for animal in self.__animals:
            if not animal.isAdopted:
                available_animals.append(animal)
        return available_animals
                
    def get_animal_by_chip(self, chip_number: str) -> Optional[Animal]:
        if not isinstance(chip_number, str):
            raise ValueError("Chip number must be a string.")
        for animal in self.__animals:
            if animal.chip_number == chip_number:
                return animal
        raise ValueError("No animal with the provided chip number exists.")

    def update_animal(self, chip_number: str, new_animal: Animal) -> Optional[Animal]:
        if not isinstance(chip_number, str) or not isinstance(new_animal, Animal):
            raise ValueError("Chip number must be a string and new_animal must be an instance of Animal class.")
        for i, animal in enumerate(self.__animals):
            if animal.chip_number == chip_number:
                self.__animals[i] = new_animal
                self.save_to_file()
                return new_animal
        raise ValueError("No animal with the provided chip number exists.")

    def delete_animal(self, chip_number: str) -> bool:
        if not isinstance(chip_number, str):
            raise ValueError("Chip number must be a string.")
        for i, animal in enumerate(self.__animals):
            if animal.chip_number == chip_number:
                del self.__animals[i]
                self.save_to_file()
                return True
        raise ValueError("No animal with the provided chip number exists.")
