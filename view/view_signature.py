from abc import ABC, abstractmethod
from datetime import date
from typing import Dict, List
from models.animal.animal import Animal
from models.registers.adoption_register import AdoptionRegister

from models.registers.donation_register import DonationRegister


class IViewSignature(ABC):

    @abstractmethod    
    def start() -> str:
        ...

    @abstractmethod    
    def get_donor_information() -> Dict[str, str]:
        ...
        # {
        #   cpf: '...'
        #   name: '...'
        #   birth_date: '...'
        #   address: '...'
        # }
    
    @abstractmethod
    def get_adopter_information() -> Dict[str, str]:
        ...
        # {
        #   cpf: '...'
        #   name: '...'
        #   birth_date: '...'
        #   address: '...'
        #   home_type: '...'
        #   has_other_pets: '...'
        # }
        
    @abstractmethod
    def get_animal_information() -> Dict[str, str]:
        ...
        # {
        # Isso monta a classe Animal
        #   chip_number: '...'
        #   name: '...'
        #   breed: '...'
        #   animal_type: '...'
        #   size: '...'
        # ------------------
        # }
        
    @abstractmethod
    def get_person_cpf_information() -> str:
        ...
    
    @abstractmethod
    def get_animal_chip_number() -> str:
        ...

    @abstractmethod
    def get_reason_donation() -> str:
        ...
        
    @abstractmethod
    def generate_donation_relatory(donations : List[DonationRegister]) -> None:
        ...
    
    @abstractmethod
    def generate_adoption_relatory(adoptions : List[AdoptionRegister]) -> None:
        ...
    
    @abstractmethod
    def generate_animal_relatory(animals : List[Animal]) -> None:
        ...
    
    @abstractmethod
    def get_period() -> date:
        ...
    
    @abstractmethod
    def sucess_message(message: str) -> str:
        ...

    @abstractmethod
    def get_vaccine() -> str:
        ...
        
    