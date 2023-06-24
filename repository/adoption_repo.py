import pickle
from datetime import date
from typing import List, Optional
from errors.client_error import ClientError
from models.registers.adoption_register import AdoptionRegister

class AdoptionRegisterRepository:
    def __init__(self):
        self.__filename = "adoptions.pkl"
        self.__adoptions: List[AdoptionRegister] = []

    def __load_data(self):
        try:
            with open(self.__filename, "rb") as f:
                self.__adoptions: List[AdoptionRegister] = pickle.load(f)
        except FileNotFoundError:
            self.__adoptions: List[AdoptionRegister] = []

    def save_to_file(self):
        with open(self.__filename, "wb") as f:
            pickle.dump(self.__adoptions, f)

    def create_adoption(self, adoption: AdoptionRegister) -> bool:
        self.__load_data()
        if not isinstance(adoption, AdoptionRegister):
            raise ClientError("adoption must be an instance of AdoptionRegister")
        
        if not isinstance(adoption.adoption_date, date):
            raise ClientError("adoption_date must be an instance of date")

        self.__adoptions.append(adoption)
        self.save_to_file()
        return True

    def read_adoption(self, cpf: str) -> Optional[AdoptionRegister]:
        self.__load_data()
        if not isinstance(cpf, str):
            raise ClientError("CPF must be a string")

        for adoption in self.__adoptions:
            if adoption.adopter.cpf == cpf:
                return adoption
        return None

    def read_all_adoptions(self) -> List[AdoptionRegister]:
        self.__load_data()
        return self.__adoptions

    def update_adoption(self, cpf: str, new_adoption: AdoptionRegister) -> bool:
        self.__load_data()
        if not isinstance(cpf, str):
            raise ClientError("CPF must be a string")

        if not isinstance(new_adoption, AdoptionRegister):
            raise ClientError("new_adoption must be an instance of AdoptionRegister")

        for i, adoption in enumerate(self.__adoptions):
            if adoption.adopter.cpf == cpf:
                self.__adoptions[i] = new_adoption
                self.save_to_file()
                return True
        return False

    def delete_adoption(self, cpf: str) -> bool:
        self.__load_data()
        if not isinstance(cpf, str):
            raise ClientError("CPF must be a string")

        for adoption in self.__adoptions:
            if adoption.adopter.cpf == cpf:
                self.__adoptions.remove(adoption)
                self.save_to_file()
                return True
        return False

    def read_all_adoptions_by_period(self, period_start: date) -> List[AdoptionRegister]:
        self.__load_data()
        period_end = date.today()
        
        if not isinstance(period_start, date):
            raise ClientError("period_start must be an instance of date")

        if not isinstance(period_end, date):
            raise ClientError("period_end must be an instance of date")

        adoptions_in_period = []
        for adoption in self.__adoptions:
            if period_start <= adoption.adoption_date <= period_end:
                adoptions_in_period.append(adoption)
        return adoptions_in_period
