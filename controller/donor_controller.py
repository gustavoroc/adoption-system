import PySimpleGUI as sg
from models.person.donor import Donor
from repository.person_repo import PersonRepository

class DonorController:
    def __init__(self, view):
        self.view = view
        self.person_repository = PersonRepository()

    def register_donor(self):
        try:
            donor_raw_data = self.view.get_donor_information()
            donor = Donor(donor_raw_data['cpf'], donor_raw_data['name'], donor_raw_data['birth_date'], donor_raw_data['address'])
            self.person_repository.create_person(donor)
            self.view.success_message(f"Doador de CPF {donor.cpf} registrado com sucesso.")
        except Exception as e:
            self.view.error_message(e)

    def update_donor(self):
        try:
            cpf = self.view.get_person_cpf_information()
            donor = self.person_repository.get_person_by_cpf(cpf)
            if isinstance(donor, Donor):
                updated_data = self.view.get_updated_donor_data()
                updated_donor = Donor(
                    cpf=donor.cpf,
                    name=updated_data['name'],
                    birth_date=donor.birth_date,
                    address=updated_data['address']
                )
                self.person_repository.update_person(cpf, updated_donor)
                self.view.success_message(f"Doador de CPF {donor.cpf} atualizado com sucesso.")
            else:
                self.view.error_message(f"Doador de CPF {cpf} não encontrado.")
        except Exception as e:
            self.view.error_message(e)

    def get_all_donors(self):
        donors = self.person_repository.get_all_donors()
        self.view.get_all_donors_view(donors)
