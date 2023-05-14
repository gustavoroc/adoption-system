from datetime import date
from typing import List, Optional
from models.registers.adoption_register import AdoptionRegister


class AdoptionRegisterRepository:
    def __init__(self):
        self.__adoptions = []

    def create_adoption(self, adoption: AdoptionRegister) -> bool:
        if not isinstance(adoption, AdoptionRegister):
            raise TypeError("adoption must be an instance of AdoptionRegister")
        
        if not isinstance(adoption.adoption_date, date):
            raise TypeError("adoption_date must be an instance of date")

        self.__adoptions.append(adoption)
        return True

    def read_adoption(self, cpf: str) -> Optional[AdoptionRegister]:
        if not isinstance(cpf, str):
            raise TypeError("CPF must be a string")

        for adoption in self.__adoptions:
            if adoption.adopter.cpf == cpf:
                return adoption
        return None

    def read_all_adoptions(self) -> List[AdoptionRegister]:
        return self.__adoptions

    def update_adoption(self, cpf: str, new_adoption: AdoptionRegister) -> bool:
        if not isinstance(cpf, str):
            raise TypeError("CPF must be a string")

        if not isinstance(new_adoption, AdoptionRegister):
            raise TypeError("new_adoption must be an instance of AdoptionRegister")

        for i, adoption in enumerate(self.__adoptions):
            if adoption.adopter.cpf == cpf:
                self.__adoptions[i] = new_adoption
                return True
        return False

    def delete_adoption(self, cpf: str) -> bool:
        if not isinstance(cpf, str):
            raise TypeError("CPF must be a string")

        for adoption in self.__adoptions:
            if adoption.adopter.cpf == cpf:
                self.__adoptions.remove(adoption)
                return True
        return False
