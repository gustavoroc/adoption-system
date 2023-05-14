from typing import Dict, List
from datetime import date
from models.animal.animal import Animal
from models.registers.adoption_register import AdoptionRegister
from models.registers.donation_register import DonationRegister
from view.view_signature import IViewSignature

class View(IViewSignature):

    def start(self) -> str:
        print('Choose a number')
        value = input('1 - Register Donor\n2 - Register Adopter\n3 - Donor Relatory\n4 - Adopter Relatory\n5 - Available Pets Relatory\n6 - Register Pet for Donation\n7 - Register Donation\n8 - Register Adoption\n9 - Vaccine Animal\n0 - Exit\n')
        return value
    
    def get_donor_information(self) -> Dict[str, str]:
        cpf = input('Please enter donor CPF: ')
        name = input('Please enter donor name: ')
        birth_date = input('Please enter donor birth date (YYYY-MM-DD): ')
        address = input('Please enter donor address: ')
        return {
            'cpf': cpf,
            'name': name,
            'birth_date': date.fromisoformat(birth_date),
            'address': address
        }
    
    def get_adopter_information(self) -> Dict[str, str]:
        cpf = input('Please enter adopter CPF: ')
        name = input('Please enter adopter name: ')
        birth_date = input('Please enter adopter birth date (YYYY-MM-DD): ')
        address = input('Please enter adopter address: ')
        home_type = input('Please enter adopter home type: ')
        has_other_pets = input('Does the adopter have other pets (Yes/No): ')
        return {
            'cpf': cpf,
            'name': name,
            'birth_date': date.fromisoformat(birth_date),
            'address': address,
            'home_type': home_type,
            'has_other_pets': has_other_pets
        }

    def get_animal_information(self) -> Dict[str, str]:
        chip_number = input('Please enter animal chip number: ')
        name = input('Please enter animal name: ')
        breed = input('Please enter animal breed: ')
        return {
            'chip_number': chip_number,
            'name': name,
            'breed': breed
        }

    def get_person_cpf_information(self) -> str:
        return input('Please enter the person CPF: ')
    
    def get_animal_chip_number(self) -> str:
        return input('Please enter the animal chip number: ')
        
    def get_reason_donation(self) -> str:
        return input('Please enter the reason for the donation: ')
        
    def generate_donation_relatory(self, donations : List[DonationRegister]) -> None:
        print('Donation Report:')
        for donation in donations:
            print(f"Date: {donation.donation_date}\nDonated Animal: {donation.donated_animal.name}\nDonor: {donation.donor.name}\nReason: {donation.reason}\n{'-'*50}")
    
    def generate_adoption_relatory(self, adoptions : List[AdoptionRegister]) -> None:
        print('Adoption Report:')
        for adoption in adoptions:
            print(f"Date: {adoption.adoption_date}\nAdopted Animal: {adoption.adopted_animal.name}\nAdopter: {adoption.adopter.name}\nSigned: {'Yes' if adoption.signed else 'No'}\n{'-'*50}")

    def generate_animal_relatory(self, animals : List[Animal]) -> None:
        print('Animal Report:')
        for animal in animals:
            print(f"Chip Number: {animal.chip_number}\nName: {animal.name}\nBreed: {animal.breed}\nAdopted: {'Yes' if animal.isAdopted else 'No'}\n{'-'*50}")

    def sucess_message(self, message: str) -> str:
        print(f'Success: {message}')

    def get_vaccine(self) -> str:
        return input('Please enter the vaccine name: ')
