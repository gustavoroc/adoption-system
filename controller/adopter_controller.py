from models.person.adopter import Adopter
from repository.person_repo import PersonRepository

class AdopterController:
    def __init__(self, view):
        self.view = view
        self.person_repository = PersonRepository()

    def register_adopter(self):
        try:
            adopter_raw_data = self.view.get_adopter_information()
            adopter = Adopter(adopter_raw_data['cpf'], adopter_raw_data['name'], adopter_raw_data['birth_date'], adopter_raw_data['address'], adopter_raw_data['home_type'], adopter_raw_data['has_other_pets'])
            self.person_repository.create_person(adopter)
            self.view.success_message(f"Adotante de cpf {adopter.cpf} registrado com sucesso.")
        except Exception as e:
            self.view.error_message(e)

    def get_all_adopters(self):
        adopters = self.person_repository.get_all_adopters()
        self.view.get_all_adopters_view(adopters)

    def delete_person(self):
            try:
                cpf = self.view.get_person_cpf_information()
                success = self.person_repository.delete_person(cpf)
                if success:
                    self.view.success_message(f"Adotante de CPF {cpf} excluído com sucesso.")
                else:
                    self.view.error_message(f"Não foi possível excluir o adotante de CPF {cpf}.")
            except Exception as e:
                self.view.error_message(e)
