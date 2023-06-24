from datetime import date
from models.registers.adoption_register import AdoptionRegister
from repository.adoption_repo import AdoptionRegisterRepository
from repository.person_repo import PersonRepository
from repository.animal_repo import AnimalRepository

class AdoptionController:
    def __init__(self, view):
        self.view = view
        self.adoption_repository = AdoptionRegisterRepository()
        self.person_repository = PersonRepository()
        self.animal_repository = AnimalRepository()

    def register_adoption(self):
        try:
            cpf = self.view.get_person_cpf_information()
            chip_number = self.view.get_animal_chip_number()
            animal = self.animal_repository.get_animal_by_chip(chip_number)
            adopter = self.person_repository.get_person_by_cpf(cpf)

            if adopter.role() == "Doador":
                raise Exception("Não é possível adotar um animal, pois o adotante é um doador.")
            
            if adopter.has_other_pets == 'yes':
                raise Exception("Não é possível adotar um animal, pois o adotante já possui outros animais.")

            if adopter.home_type == "small" and animal.size != "small":
                raise Exception("Não é possível adotar um cachorro, pois o adotante mora em apartamento.")
            
            if not animal.vaccine_history.check_vaccines():
                raise Exception("Não é possível adotar um animal, pois o animal não possui todas as vacinas obrigatórias.")
            
            if not adopter.check_adult():
                raise Exception("Não é possível adotar um animal, pois o adotante não é maior de idade.")

            adoption = AdoptionRegister(date.today(), animal, adopter, True)
            animal.isAdopted = True

            self.animal_repository.update_animal(animal.chip_number, animal)
            self.adoption_repository.create_adoption(adoption)
            self.view.success_message(f'Animal de chip {animal.chip_number} adotado com sucesso pelo adotante de cpf: {adopter.cpf}.')
        except Exception as e:
            self.view.error_message(e)
