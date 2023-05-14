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