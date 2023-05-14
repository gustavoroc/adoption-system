from datetime import date
from models.person.person import Person


class Donor(Person):

    def __init__(self, cpf: str, name: str, birth_date: date, address: str):
        super().__init__(cpf, name, birth_date, address)

    def role(self):
        return "Doador"
    
