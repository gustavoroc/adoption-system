from abc import ABC, abstractmethod
from typing import Dict


class IViewSignature(ABC):

    @abstractmethod    
    def start():
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
        #   chip_number: '...'
        #   name: '...'
        #   breed: '...'
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
    def sucess_message(message: str) -> str:
        ...

    @abstractmethod
    def get_vaccine() -> str:
        ...
        
    