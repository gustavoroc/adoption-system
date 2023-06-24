from controller.donor_controller import DonorController
from controller.adopter_controller import AdopterController
from controller.report_controller import ReportController
from controller.pet_controller import PetController
from controller.donation_controller import DonationController
from controller.adoption_controller import AdoptionController
from controller.vaccine_controller import VaccineController
from view.view import View

def main():
    view = View()
    donor_controller = DonorController(view)
    adopter_controller = AdopterController(view)
    report_controller = ReportController(view)
    pet_controller = PetController(view)
    donation_controller = DonationController(view)
    adoption_controller = AdoptionController(view)
    vaccine_controller = VaccineController(view)

    while True:
        action = view.start()
        if action == '1':
            donor_controller.register_donor()
        elif action == '2':
            adopter_controller.register_adopter()
        elif action == '3':
            report_controller.donor_report()
        elif action == '4':
            report_controller.adopter_report()
        elif action == '5':
            report_controller.available_pets_report()
        elif action == '6':
            pet_controller.register_pet_for_donation()
        elif action == '7':
            donation_controller.register_donation()
        elif action == '8':
            adoption_controller.register_adoption()
        elif action == '9':
            vaccine_controller.vaccine_animal()
        elif action == '10':
            report_controller.adopter_report_by_period()
        elif action == '11':
            report_controller.donor_report_by_period()
        elif action == '12':
            pet_controller.update_animal()
        elif action == '13':
            donor_controller.update_donor()
        elif action == '14':
            donor_controller.get_all_donors()
        elif action == '15':
            adopter_controller.get_all_adopters()
        elif action == '16':
            adopter_controller.delete_person()
        elif action == '17':
            pet_controller.delete_animal()
        elif action == '0':
            break

if __name__ == "__main__":
    main()
