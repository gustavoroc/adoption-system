from typing import Dict, List
from datetime import date
from models.animal.animal import Animal
from models.registers.adoption_register import AdoptionRegister
from models.registers.donation_register import DonationRegister
from view.view_signature import IViewSignature

import PySimpleGUI as sg

class View(IViewSignature):
    def start(self):
        # Criar layout
        layout = [
            [sg.Text('Escolha um número')],
            [sg.Button('1 - Registrar Doador', key='1')],
            [sg.Button('2 - Registrar Adotante', key='2')],
            [sg.Button('3 - Relatório do Doador', key='3')],
            [sg.Button('4 - Relatório do Adotante', key='4')],
            [sg.Button('5 - Relatório de Pets Disponíveis', key='5')],
            [sg.Button('6 - Registrar Pet para Doação', key='6')],
            [sg.Button('7 - Registrar Doação', key='7')],
            [sg.Button('8 - Registrar Adoção', key='8')],
            [sg.Button('9 - Vacinar Animal', key='9')],
            [sg.Button('10 - Relatório de Adoção por Data', key='10')],
            [sg.Button('11 - Relatório de Doação por Data', key='11')],
            [sg.Button('0 - Sair', key='0')],
        ]

        window = sg.Window('Escolha uma Opção', layout)
        x = window.read()       
        window.close()

        return (x[0])

    def get_donor_information(self):
        layout = [
            [sg.Text('Por favor, insira o CPF do doador:'), sg.InputText(key='cpf')],
            [sg.Text('Por favor, insira o nome do doador:'), sg.InputText(key='name')],
            [sg.Text('Por favor, insira a data de nascimento do doador (AAAA-MM-DD):'), sg.InputText(key='birth_date')],
            [sg.Text('Por favor, insira o endereço do doador:'), sg.InputText(key='address')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Informações do Doador', layout)

       
        event, values = window.read()
        window.close()
        
        return {
                'cpf': values['cpf'],
                'name': values['name'],
                'birth_date': date.fromisoformat(values['birth_date']),
                'address': values['address']
           }
    
    def get_adopter_information(self):
        layout = [
            [sg.Text('Por favor, insira o CPF do adotante:'), sg.InputText(key='cpf')],
            [sg.Text('Por favor, insira o nome do adotante:'), sg.InputText(key='name')],
            [sg.Text('Por favor, insira a data de nascimento do adotante (AAAA-MM-DD):'), sg.InputText(key='birth_date')],
            [sg.Text('Por favor, insira o endereço do adotante:'), sg.InputText(key='address')],
            [sg.Text('Por favor, insira o tipo de residência do adotante (pequeno|médio|grande):'), sg.InputText(key='home_type')],
            [sg.Text('O adotante possui outros pets (sim/não):'), sg.InputText(key='has_other_pets')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Informações do Adotante', layout)
        event, values = window.read()

        window.close()

        return {
                'cpf': values['cpf'],
                'name': values['name'],
                'birth_date': date.fromisoformat(values['birth_date']),
                'address': values['address'],
                'home_type': values['home_type'],
                'has_other_pets': values['has_other_pets']
        }
    
    def get_animal_information(self):
        layout = [
            [sg.Text('Por favor, insira o número do chip do animal:'), sg.InputText(key='chip_number')],
            [sg.Text('Por favor, insira o nome do animal:'), sg.InputText(key='name')],
            [sg.Text('Por favor, insira a raça do animal:'), sg.InputText(key='breed')],
            [sg.Text('Por favor, insira o tipo de animal (cão|gato):'), sg.InputText(key='animal_type')],
            [sg.Text('Por favor, insira o porte do animal (pequeno|médio|grande):'), sg.InputText(key='size')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Informações do Animal', layout)

        event, values = window.read()
        window.close()

        animal_type = values['animal_type']
        size = values['size'] if animal_type.lower() == 'dog' else 'small'

        return {
            'chip_number': values['chip_number'],
            'name': values['name'],
            'breed': values['breed'],
            'animal_type': animal_type,
            'size': size
        }

    def get_person_cpf_information(self):
        layout = [
            [sg.Text('Por favor, insira o CPF da pessoa:'), sg.InputText(key='cpf')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Informações do CPF', layout)

        event, values = window.read()
        window.close()

        return values['cpf']
    
    def get_animal_chip_number(self) -> str:
        layout = [
            [sg.Text('Por favor, insira o número do chip do animal:'), sg.InputText(key='chip_number')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Informações do Chip do Animal', layout)

        event, values = window.read()
        window.close()

        return values['chip_number']
   
    def get_reason_donation(self) -> str:
        layout = [
            [sg.Text('Por favor, insira o motivo da doação:'), sg.InputText(key='reason')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Motivo da Doação', layout)

        event, values = window.read()
        window.close()

        return values['reason']
     
    def generate_donation_relatory(self, donations: List[DonationRegister]) -> None:
        layout = [
            [sg.Text('Donation Report:')],
            [sg.Text('', key='output', size=(50, len(donations) * 5))],
            [sg.Button('OK')]
        ]

        window = sg.Window('Relatório de Doações', layout)

        output_text = ''
        for donation in donations:
            output_text += f"Date: {donation.donation_date}\nDonated Animal: {donation.donated_animal.name}\nDonor: {donation.donor.name}\nReason: {donation.reason}\n{'-' * 50}\n"

        window['output'].update(output_text)

        event, values = window.read()
        window.close()
    
    def generate_adoption_relatory(self, adoptions: List[AdoptionRegister]) -> None:
        layout = [
            [sg.Text('Adoption Report:')],
            [sg.Text('', key='output', size=(50, len(adoptions) * 5))],
            [sg.Button('OK')]
        ]

        window = sg.Window('Relatório de Adoções', layout)

        output_text = ''
        for adoption in adoptions:
            output_text += f"Date: {adoption.adoption_date}\nAdopted Animal: {adoption.adopted_animal.name}\nAdopter: {adoption.adopter.name}\nSigned: {'Yes' if adoption.signed else 'No'}\n{'-' * 50}\n"

        window['output'].update(output_text)

        event, values = window.read()
        window.close()

    def generate_animal_relatory(self, animals: List[Animal]) -> None:
        layout = [
            [sg.Text('Animal Report:')],
            [sg.Text('', key='output', size=(50, len(animals) * 5))],
            [sg.Button('OK')]
        ]

        window = sg.Window('Relatório de Animais', layout)

        output_text = ''
        for animal in animals:
            output_text += f"Chip Number: {animal.chip_number}\nName: {animal.name}\nBreed: {animal.breed}\nAdopted: {'Yes' if animal.isAdopted else 'No'}\n{'-' * 50}\n"

        window['output'].update(output_text)

        event, values = window.read()
        window.close()

    def get_period(self) -> date:
        layout = [
            [sg.Text('Please enter a date (YYYY-MM-DD):'), sg.InputText(key='date')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Período', layout)

        event, values = window.read()
        window.close()

        date_time = values['date']
        return date.fromisoformat(date_time)
 
    def success_message(self, message: str) -> str:
        layout = [
            [sg.Text(f'Success: {message}')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Mensagem de Sucesso', layout)

        event, values = window.read()
        window.close()

        return message

    def get_vaccine(self) -> str:
        layout = [
            [sg.Text('Please enter the vaccine name:'), sg.InputText(key='vaccine')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Nome da Vacina', layout)

        event, values = window.read()
        window.close()

        return values['vaccine']
