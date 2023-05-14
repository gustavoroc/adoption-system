from controller.controller import Controller
from repository.adoption_repo import AdoptionRegisterRepository
from repository.animal_repo import AnimalRepository
from repository.donation_repo import DonationRegisterRepository
from repository.person_repo import PersonRepository
from view.view import View


controller = Controller(View(), PersonRepository(), AnimalRepository(), DonationRegisterRepository(), AdoptionRegisterRepository())

while True:
    if (controller.start_view() == '00'):
        break