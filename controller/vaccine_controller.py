from datetime import date
from models.vaccine.vaccine import Vaccine
from repository.animal_repo import AnimalRepository

class VaccineController:
    def __init__(self, view):
        self.view = view
        self.animal_repository = AnimalRepository()

    def vaccine_animal(self):
        try:
            chip_id = self.view.get_animal_chip_number()
            vaccine_name = self.view.get_vaccine()

            animal = self.animal_repository.get_animal_by_chip(chip_id)
            vaccine = Vaccine(vaccine_name, date.today())
            animal.vaccine_history.add_vaccine(vaccine)

            self.animal_repository.update_animal(animal.chip_number, animal)
            self.view.success_message(f"Vacina {vaccine.name} adicionada ao animal de chip {animal.chip_number} com sucesso.")
        except Exception as e:
            self.view.error_message(e)
