from repository.donation_repo import DonationRegisterRepository
from repository.adoption_repo import AdoptionRegisterRepository
from repository.animal_repo import AnimalRepository

class ReportController:
    def __init__(self, view):
        self.view = view
        self.donation_repository = DonationRegisterRepository()
        self.adoption_repository = AdoptionRegisterRepository()
        self.animal_repository = AnimalRepository()

    def donor_report(self):
        try:
            donations = self.donation_repository.read_all_donations()
            self.view.generate_donation_report(donations)
            self.view.success_message(f"{len(donations)} doações foram registradas.")
        except Exception as e:
            self.view.error_message(e)

    def adopter_report(self):
        try:
            adoptions = self.adoption_repository.read_all_adoptions()
            self.view.generate_adoption_report(adoptions)
            self.view.success_message(f"{len(adoptions)} adoções foram registradas.")
        except Exception as e:
            self.view.error_message(e)

    def available_pets_report(self):
        try:
            animals = self.animal_repository.get_available_animals()
            self.view.generate_animal_report(animals)
            self.view.success_message(f"Há {len(animals)} animais disponíveis para adoção.")
        except Exception as e:
            self.view.error_message(e)

    def adopter_report_by_period(self):
        try:
            date = self.view.get_period()
            adoptions = self.adoption_repository.read_all_adoptions_by_period(date)
            self.view.generate_adoption_report(adoptions)
            self.view.success_message(f"Há {len(adoptions)} adoções no período {date.strftime('%Y-%m-%d')} - {date.today().strftime('%Y-%m-%d')}")
        except Exception as e:
            self.view.error_message(e)

    def donor_report_by_period(self):
        try:
            date = self.view.get_period()
            donations = self.donation_repository.read_all_donations_by_period(date)
            self.view.generate_donation_report(donations)
            self.view.success_message(f"Há {len(donations)} doações no período {date.strftime('%Y-%m-%d')} - {date.today().strftime('%Y-%m-%d')}")
        except Exception as e:
            self.view.error_message(e)
