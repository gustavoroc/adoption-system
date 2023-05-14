from typing import List, Optional
from models.person.adopter import Adopter
from models.person.donor import Donor
from models.person.person import Person

class PersonRepository:
    def __init__(self):
        self.__people: List[Person] = []

    def create_person(self, person: Person) -> None:
        if not isinstance(person, Person):
            raise ValueError("Input must be an instance of Person class.")
        for existing_person in self.__people:
            if existing_person.cpf == person.cpf:
                raise ValueError("A person with the same CPF already exists.")
        self.__people.append(person)

    def get_all_people(self) -> List[Person]:
        return self.__people

    def get_person_by_cpf(self, cpf: str) -> Optional[Person]:
        if not isinstance(cpf, str):
            raise ValueError("CPF must be a string.")
        for person in self.__people:
            if person.cpf == cpf:
                return person
        raise ValueError("No person with the provided CPF exists.")

    def update_person(self, cpf: str, new_person: Person) -> Optional[Person]:
        if not isinstance(cpf, str) or not isinstance(new_person, Person):
            raise ValueError("CPF must be a string and new_person must be an instance of Person class.")
        for i, person in enumerate(self.__people):
            if person.cpf == cpf:
                self.__people[i] = new_person
                return new_person
        raise ValueError("No person with the provided CPF exists.")

    def delete_person(self, cpf: str) -> bool:
        if not isinstance(cpf, str):
            raise ValueError("CPF must be a string.")
        for i, person in enumerate(self.__people):
            if person.cpf == cpf:
                del self.__people[i]
                return True
        raise ValueError("No person with the provided CPF exists.")
    
    def get_all_donors(self) -> List[Donor]:
        return [person for person in self.__people if isinstance(person, Donor)]
    
    def get_all_adopters(self) -> List[Adopter]:
        return [person for person in self.__people if isinstance(person, Adopter)]
