from models.animal.cat import Cat
from models.animal.dog import Dog
from repository.animal_repo import AnimalRepository

class PetController:
    def __init__(self, view):
        self.view = view
        self.animal_repository = AnimalRepository()

    def register_pet_for_donation(self):
        try:
            animal_raw_data = self.view.get_animal_information()

            if animal_raw_data['animal_type'] == "cat":
                animal = Cat(animal_raw_data['chip_number'], animal_raw_data['name'], animal_raw_data['breed'])
            else:
                animal = Dog(animal_raw_data['chip_number'], animal_raw_data['name'], animal_raw_data['breed'], animal_raw_data['size'])

            self.animal_repository.create_animal(animal)
            self.view.success_message(f"{animal.animal_type()} de chip {animal.chip_number} foi registrado com sucesso.")
        except Exception as e:
            self.view.error_message(e)

    def update_animal(self):
        try:
            chip_number = self.view.get_animal_chip_number()
            updated_animal_data = self.view.get_updated_animal_data()
            
            existing_animal = self.animal_repository.get_animal_by_chip(chip_number)
            if not existing_animal:
                self.view.error_message(f"Animal com chip {chip_number} não encontrado.")
                return
            
            if existing_animal.animal_type() == "cat":
                updated_animal = Cat(chip_number, updated_animal_data['name'], updated_animal_data['breed'])
            else:
                updated_animal = Dog(chip_number, updated_animal_data['name'], updated_animal_data['breed'], updated_animal_data['size'])

            self.animal_repository.update_animal(chip_number, updated_animal)
            self.view.success_message(f"Animal de chip {chip_number} foi atualizado com sucesso.")
        except Exception as e:
            self.view.error_message(str(e))

    def delete_animal(self):
        chip_number = self.view.get_animal_chip_number()
        try:
            deleted_animal = self.animal_repository.delete_animal(chip_number)
            if deleted_animal:
                self.view.success_message(f"Animal com chip {chip_number} excluído com sucesso.")
            else:
                self.view.error_message("Nenhum animal com o chip fornecido foi encontrado.")
        except Exception as e:
            self.view.error_message(str(e))


