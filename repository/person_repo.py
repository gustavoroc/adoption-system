import pickle
from typing import List, Optional
from errors.client_error import ClientError
from errors.duplicated_instance_error import DuplicatedInstanceError

from models.person.adopter import Adopter
from models.person.donor import Donor
from models.person.person import Person

class PersonRepository:
    def __init__(self):
        self.__filename = "people.pkl"
        self.__people: List[Person] = []

    def __load_data(self):
        try:
            with open(self.__filename, "rb") as f:
                self.__people: List[Person] = pickle.load(f)
        except FileNotFoundError:
            self.__people: List[Person] = []

    def save_to_file(self):
        with open(self.__filename, "wb") as f:
            pickle.dump(self.__people, f)

    def create_person(self, person: Person) -> None:
        self.__load_data()
        if not isinstance(person, Person):
            raise ClientError("Input must be an instance of Person class.")
        for existing_person in self.__people:
            if existing_person.cpf == person.cpf:
                raise DuplicatedInstanceError("A person with the same CPF already exists.")
        self.__people.append(person)
        self.save_to_file()

    def get_all_people(self) -> List[Person]:
        self.__load_data()
        return self.__people

    def get_person_by_cpf(self, cpf: str) -> Optional[Person]:
        self.__load_data()
        if not isinstance(cpf, str):
            raise ClientError("CPF must be a string.")
        for person in self.__people:
            if person.cpf == cpf:
                return person
        raise ClientError("No person with the provided CPF exists.")

    def update_person(self, cpf: str, new_person: Person) -> Optional[Person]:
        self.__load_data()
        if not isinstance(cpf, str) or not isinstance(new_person, Person):
            raise ClientError("CPF must be a string and new_person must be an instance of Person class.")
        for i, person in enumerate(self.__people):
            if person.cpf == cpf:
                self.__people[i] = new_person
                self.save_to_file()
                return new_person
        raise ClientError("No person with the provided CPF exists.")

    def delete_person(self, cpf: str) -> bool:
        self.__load_data()
        if not isinstance(cpf, str):
            raise ClientError("CPF must be a string.")
        for i, person in enumerate(self.__people):
            if person.cpf == cpf:
                del self.__people[i]
                self.save_to_file()
                return True
        raise ClientError("No person with the provided CPF exists.")
    
    def get_all_donors(self) -> List[Donor]:
        self.__load_data()
        return [person for person in self.__people if isinstance(person, Donor)]
    
    def get_all_adopters(self) -> List[Adopter]:
        self.__load_data()
        return [person for person in self.__people if isinstance(person, Adopter)]
