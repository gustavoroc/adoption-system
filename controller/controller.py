from datetime import date
from models.person.adopter import Adopter
from models.person.donor import Donor
from repository.person_repo import PersonRepository
from view.view_signature import IViewSignature

class Controller:
    def __init__(self, viewService: IViewSignature, person_repository: PersonRepository):
        self.__viewService = viewService
        self.__personRepository = person_repository
        
        self.viewCommand = {
            '1': lambda: self.register_donor(),
            '2': lambda: self.register_adopter(),
            '3': lambda: self.donor_relatory(),
            '4': lambda: self.adopter_relatory(),
            '5': lambda: self.pet_relatory(),
            '6': lambda: self.register_pet_for_donation()
        }

    def start_view(self):
        try:
            view_target_action = self.__viewService.start() 
            self.viewCommand[view_target_action]()
        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")

    def register_donor(self):
        try:
            donor_raw_data = self.__viewService.get_donor_information()
            donor = Donor(donor_raw_data['cpf'], donor_raw_data['name'], donor_raw_data['birth_date'], donor_raw_data['address'])
            self.__personRepository.create_person(donor)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        
    def register_adopter(self):
        try:
            adopter_raw_data = self.__viewService.get_adopter_information()
            adopter = Adopter(adopter_raw_data['cpf'], adopter_raw_data['name'], adopter_raw_data['birth_date'], adopter_raw_data['address'], adopter_raw_data['home_type'], adopter_raw_data['has_other_pets'])
            self.__personRepository.create_person(adopter)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def register_pet_for_donation():
        ...

    def donor_relatory():
        # Deve retornar um relatório de doadores;
        ...

    def adopter_relatory():
        # Deve retornar um relatório de adotantes;
        ...

    def pet_relatory():
        # Deve retornar um relatório de pets;
        ...
