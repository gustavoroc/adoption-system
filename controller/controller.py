from datetime import date
from models.animal.animal import Animal
from models.person.adopter import Adopter
from models.person.donor import Donor
from models.registers.donation_register import DonationRegister
from repository.adoption_repo import AdoptionRegisterRepository
from repository.animal_repo import AnimalRepository
from repository.donation_repo import DonationRegisterRepository
from repository.person_repo import PersonRepository
from view.view_signature import IViewSignature

class Controller:
    def __init__(self, viewService: IViewSignature, person_repository: PersonRepository, animal_repository: AnimalRepository, donation_repository: DonationRegisterRepository, adoption_repository: AdoptionRegisterRepository):
        self.__viewService = viewService
        self.__personRepository = person_repository
        self.__animalRepository = animal_repository
        self.__donationRepository = donation_repository
        self.__adoptionRepository = adoption_repository
        
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
            self.__viewService.sucess_message(f"Doador de cpf {donor.cpf} registrado com sucesso.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        
    def register_adopter(self):
        try:
            adopter_raw_data = self.__viewService.get_adopter_information()
            adopter = Adopter(adopter_raw_data['cpf'], adopter_raw_data['name'], adopter_raw_data['birth_date'], adopter_raw_data['address'], adopter_raw_data['home_type'], adopter_raw_data['has_other_pets'])
            self.__personRepository.create_person(adopter)
            self.__viewService.sucess_message(f"Adotante de cpf {adopter.cpf} registrado com sucesso.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def register_pet_for_donation(self):
        try:
            animal_raw_data = self.__viewService.get_animal_information()
            animal = Animal(animal_raw_data['chip_number'], animal_raw_data['name'], animal_raw_data['breed'])
            self.__animalRepository.create_animal(animal)
            self.__viewService.sucess_message(f"{animal.animal_type} de chip {animal.chip_number} foi registrado com sucesso.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    
    def register_donation(self):
        try:
            donator_cpf = self.__viewService.get_person_cpf_information()
            animal_chip_number = self.__viewService.get_animal_chip_number()
            reason_for_donation = self.__viewService.get_reason_donation()
            current_date = date.today()
            
            animal = self.__animalRepository.get_animal_by_chip(animal_chip_number)
            donator = self.__personRepository.get_person_by_cpf(donator_cpf)
            
            donation = DonationRegister(current_date, animal, donator, reason_for_donation)
            
            self.__donationRepository.create_donation(donation)
            self.__viewService.sucess_message(f"A doação do animal {animal.name} foi concluida com sucesso.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    
    def register_adoption(self):
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
