import pickle
from datetime import date
from typing import List, Optional
from errors.client_error import ClientError
from errors.duplicated_instance_error import DuplicatedInstanceError
from models.registers.donation_register import DonationRegister

class DonationRegisterRepository:
    def __init__(self):
        self.__filename = "donations.pkl"
        self.__donations: List[DonationRegister] = []

    def __load_data(self):
        try:
            with open(self.__filename, "rb") as f:
                self.__donations: List[DonationRegister] = pickle.load(f)
        except FileNotFoundError:
            self.__donations: List[DonationRegister] = []

    def save_to_file(self):
        with open(self.__filename, "wb") as f:
            pickle.dump(self.__donations, f)

    def create_donation(self, donation: DonationRegister) -> bool:
        self.__load_data()
        if not isinstance(donation, DonationRegister):
            raise ClientError("donation must be an instance of DonationRegister")

        if not isinstance(donation.donation_date, date):
            raise ClientError("donation_date must be an instance of date")
        
        # check if the dog is already registered in the donations list
        for donationOfTheArray in self.__donations:
            if donationOfTheArray.donated_animal.chip_number == donation.donated_animal.chip_number:
                raise DuplicatedInstanceError("This dog is already registered in the donations list")

        self.__donations.append(donation)
        self.save_to_file()
        return True

    def read_donation(self, cpf: str) -> Optional[DonationRegister]:
        self.__load_data()
        if not isinstance(cpf, str):
            raise ClientError("CPF must be a string")

        for donation in self.__donations:
            if donation.donor.cpf == cpf:
                return donation
        return None

    def read_all_donations(self) -> List[DonationRegister]:
        self.__load_data()
        return self.__donations

    def update_donation(self, cpf: str, new_donation: DonationRegister) -> bool:
        self.__load_data()
        if not isinstance(cpf, str):
            raise ClientError("CPF must be a string")

        if not isinstance(new_donation, DonationRegister):
            raise ClientError("new_donation must be an instance of DonationRegister")

        for i, donation in enumerate(self.__donations):
            if donation.donor.cpf == cpf:
                self.__donations[i] = new_donation
                self.save_to_file()
                return True
        return False

    def delete_donation(self, cpf: str) -> bool:
        self.__load_data()
        if not isinstance(cpf, str):
            raise ClientError("CPF must be a string")

        for donation in self.__donations:
            if donation.donor.cpf == cpf:
                self.__donations.remove(donation)
                self.save_to_file()
                return True
        return False

    def read_all_donations_by_period(self, period_start: date) -> List[DonationRegister]:
        self.__load_data()
        period_end = date.today()
        
        if not isinstance(period_start, date):
            raise ClientError("period_start must be an instance of date")

        if not isinstance(period_end, date):
            raise ClientError("period_end must be an instance of date")

        donations_in_period = []
        for donation in self.__donations:
            if period_start <= donation.donation_date <= period_end:
                donations_in_period.append(donation)
        return donations_in_period
