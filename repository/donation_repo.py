from datetime import date
from typing import List, Optional
from models.registers.donation_register import DonationRegister


class DonationRegisterRepository:
    def __init__(self):
        self.__donations: List[DonationRegister] = []

    def create_donation(self, donation: DonationRegister) -> bool:
        if not isinstance(donation, DonationRegister):
            raise TypeError("donation must be an instance of DonationRegister")

        if not isinstance(donation.donation_date, date):
            raise TypeError("donation_date must be an instance of date")
        
        # check if the dog is already registered in the donations list
        for donationOfTheArray in self.__donations:
            if donationOfTheArray.donated_animal.chip_number == donation.donated_animal.chip_number:
                raise TypeError("This dog is already registered in the donations list")

        self.__donations.append(donation)
        return True

    def read_donation(self, cpf: str) -> Optional[DonationRegister]:
        if not isinstance(cpf, str):
            raise TypeError("CPF must be a string")

        for donation in self.__donations:
            if donation.donor.cpf == cpf:
                return donation
        return None

    def read_all_donations(self) -> List[DonationRegister]:
        return self.__donations

    def update_donation(self, cpf: str, new_donation: DonationRegister) -> bool:
        if not isinstance(cpf, str):
            raise TypeError("CPF must be a string")

        if not isinstance(new_donation, DonationRegister):
            raise TypeError("new_donation must be an instance of DonationRegister")

        for i, donation in enumerate(self.__donations):
            if donation.donor.cpf == cpf:
                self.__donations[i] = new_donation
                return True
        return False

    def delete_donation(self, cpf: str) -> bool:
        if not isinstance(cpf, str):
            raise TypeError("CPF must be a string")

        for donation in self.__donations:
            if donation.donor.cpf == cpf:
                self.__donations.remove(donation)
                return True
        return False