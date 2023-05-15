from datetime import date
from models.animal.animal import Animal
from models.animal.cat import Cat
from models.animal.dog import Dog
from models.person.adopter import Adopter
from models.person.donor import Donor
from models.registers.adoption_register import AdoptionRegister
from models.registers.donation_register import DonationRegister
from models.vaccine.vaccine import Vaccine
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
            '5': lambda: self.available_pets_relatory(),
            '6': lambda: self.register_pet_for_donation(),
            '7': lambda: self.register_donation(),
            '8': lambda: self.register_adoption(),
            '9': lambda: self.vaccine_animal(),
            '10': lambda: self.adopter_relatory_by_period(),
            '11': lambda: self.donor_relatory_by_period(),
            '0': lambda: self.exit()
        }

    def exit(self):
        return '00'

    def start_view(self):
        try:
            view_target_action = self.__viewService.start() 
            return self.viewCommand[view_target_action]()
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

            if (animal_raw_data['animal_type'] == "cat"):
               animal =  Cat(animal_raw_data['chip_number'], animal_raw_data['name'], animal_raw_data['breed'])
            else:
                animal = Dog(animal_raw_data['chip_number'], animal_raw_data['name'], animal_raw_data['breed'], animal_raw_data['size'])

            self.__animalRepository.create_animal(animal)
            self.__viewService.sucess_message(f"{animal.animal_type()} de chip {animal.chip_number} foi registrado com sucesso.")
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
        try:
            cpf = self.__viewService.get_person_cpf_information()
            chip_number = self.__viewService.get_animal_chip_number()
            animal = self.__animalRepository.get_animal_by_chip(chip_number)
            adopter = self.__personRepository.get_person_by_cpf(cpf)

            if (adopter.role() == "Doador"):
                raise Exception("Não é possível adotar um animal, pois o adotante é um doador.")
            
            if (adopter.has_other_pets == 'yes'):
                raise Exception("Não é possível adotar um animal, pois o adotante já possui outros animais.")

            if(adopter.home_type == "small" and animal.size != "small"):
                raise Exception("Não é possível adotar um cachorro, pois o adotante mora em apartamento.")
            
            if(not animal.vaccine_history.check_vaccines()):
                raise Exception("Não é possível adotar um animal, pois o animal não possui todas as vacinas obrigatórias.")
            
            if (not adopter.check_adult()):
                raise Exception("Não é possível adotar um animal, pois o adotante não é maior de idade.")

            adoption = AdoptionRegister(date.today(), animal, adopter, True)
            animal.isAdopted = True

            self.__animalRepository.update_animal(animal.chip_number, animal)
            self.__adoptionRepository.create_adoption(adoption)
            self.__viewService.sucess_message(f'Animal de chip {animal.chip_number} adotado com sucesso pelo adotante de cpf: {adopter.cpf}.')
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def vaccine_animal(self):
        try:
            chip_id = self.__viewService.get_animal_chip_number()
            vaccine_name = self.__viewService.get_vaccine()

            animal = self.__animalRepository.get_animal_by_chip(chip_id)
            vaccine = Vaccine(vaccine_name, date.today())
            animal.vaccine_history.add_vaccine(vaccine)

            self.__animalRepository.update_animal(animal.chip_number, animal)
            self.__viewService.sucess_message(f"Vacina {vaccine.name} adicionada ao animal de chip {animal.chip_number} com sucesso.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def donor_relatory(self):
        try:
            donations = self.__donationRepository.read_all_donations()
            self.__viewService.generate_donation_relatory(donations)
            self.__viewService.sucess_message(f"{len(donations)} de doações foram feitas")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def adopter_relatory(self):
        try: 
            adoptions = self.__adoptionRepository.read_all_adoptions()
            self.__viewService.generate_adoption_relatory(adoptions)
            self.__viewService.sucess_message(f"{len(adoptions)} de adoções foram feitas")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def available_pets_relatory(self):
        try:
            animals = self.__animalRepository.get_available_animals()
            self.__viewService.generate_animal_relatory(animals)
            self.__viewService.sucess_message(f"Há {len(animals)} animais disponíveis para adoação")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        
    def adopter_relatory_by_period(self):
        try:
            date = self.__viewService.get_period()
            adoptions = self.__adoptionRepository.read_all_adoptions_by_period(date)
            self.__viewService.generate_adoption_relatory(adoptions)
            self.__viewService.sucess_message(f"Há {len(adoptions)} adoções no período {date.strftime('%Y-%m-%d')} - {date.today().strftime('%Y-%m-%d')})")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    
    def donor_relatory_by_period(self):
        try:
            date = self.__viewService.get_period()
            donations = self.__donationRepository.read_all_donations_by_period(date)
            self.__viewService.generate_donation_relatory(donations)
            self.__viewService.sucess_message(f"Há {len(donations)} doações no período {date.strftime('%Y-%m-%d')} - {date.today().strftime('%Y-%m-%d')})")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")