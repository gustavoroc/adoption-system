from datetime import date
from models.registers.donation_register import DonationRegister
from repository.donation_repo import DonationRegisterRepository
from repository.person_repo import PersonRepository
from repository.animal_repo import AnimalRepository

class DonationController:
    def __init__(self, view):
        self.view = view
        self.donation_repository = DonationRegisterRepository()
        self.person_repository = PersonRepository()
        self.animal_repository = AnimalRepository()

    def register_donation(self):
        try:
            donator_cpf = self.view.get_person_cpf_information()
            animal_chip_number = self.view.get_animal_chip_number()
            reason_for_donation = self.view.get_reason_donation()
            current_date = date.today()
            
            animal = self.animal_repository.get_animal_by_chip(animal_chip_number)
            donator = self.person_repository.get_person_by_cpf(donator_cpf)
            
            donation = DonationRegister(current_date, animal, donator, reason_for_donation)
            
            self.donation_repository.create_donation(donation)
            self.view.success_message(f"A doação do animal {animal.name} foi concluída com sucesso.")
        except Exception as e:
            self.view.error_message(e)


