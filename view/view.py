from typing import List
from datetime import date
from models.animal.animal import Animal
from models.person.adopter import Adopter
from models.person.donor import Donor
from models.registers.adoption_register import AdoptionRegister
from models.registers.donation_register import DonationRegister

import PySimpleGUI as sg

class View:
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
            [sg.Button('12 - Atualizar Animal', key='12')],
            [sg.Button('13 - Atualizar Doador', key='13')],
            [sg.Button('14 - Listar Doadores', key='14')],
            [sg.Button('15 - Listar Adotantes', key='15')],
            [sg.Button('16 - Deletar Pessoa', key='16')],
            [sg.Button('17 - Deletar Animal', key='17')],
            [sg.Button('0 - Sair', key='0')],
        ]

        window = sg.Window('Escolha uma Opção', layout)
        event, _ = window.read()       
        window.close()

        return event

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
     
    def generate_donation_report(self, donations: List[DonationRegister]) -> None:
        output_text = ''
        for donation in donations:
            output_text += f"Data: {donation.donation_date}\nAnimal doado: {donation.donated_animal.name}\nDoador: {donation.donor.name}\nMotivo: {donation.reason}\n{'-' * 50}\n"

        layout = [
            [sg.Text('Relatório de Doações:')],
            [sg.Multiline(output_text, size=(50, len(donations) * 5), disabled=True)],
            [sg.Button('OK')]
        ]

        window = sg.Window('Relatório de Doações', layout)
        event, _ = window.read()
        window.close()

    def generate_adoption_report(self, adoptions: List[AdoptionRegister]) -> None:
        output_text = ''
        for adoption in adoptions:
            output_text += f"Data: {adoption.adoption_date}\nAnimal adotado: {adoption.adopted_animal.name}\nAdotante: {adoption.adopter.name}\nAssinado: {'Sim' if adoption.signed else 'Não'}\n{'-' * 50}\n"

        layout = [
            [sg.Text('Relatório de Adoções:')],
            [sg.Multiline(output_text, size=(50, len(adoptions) * 5), disabled=True)],
            [sg.Button('OK')]
        ]

        window = sg.Window('Relatório de Adoções', layout)
        event, _ = window.read()
        window.close()

    def generate_animal_report(self, animals: List[Animal]) -> None:
        output_text = ''
        for animal in animals:
            output_text += f"Número do Chip: {animal.chip_number}\nNome: {animal.name}\nRaça: {animal.breed}\nAdotado: {'Sim' if animal.isAdopted else 'Não'}\n{'-' * 50}\n"

        layout = [
            [sg.Text('Relatório de Animais:')],
            [sg.Multiline(output_text, size=(50, len(animals) * 5), disabled=True)],
            [sg.Button('OK')]
        ]

        window = sg.Window('Relatório de Animais', layout)
        event, _ = window.read()
        window.close()


    def get_period(self) -> date:
        layout = [
            [sg.Text('Por favor, insira uma data (AAAA-MM-DD):'), sg.InputText(key='date')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Período', layout)
        event, values = window.read()
        window.close()

        date_str = values['date']
        return date.fromisoformat(date_str)
 
    def success_message(self, message: str) -> None:
        layout = [
            [sg.Text(f'Sucesso: {message}')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Mensagem de Sucesso', layout)
        event, _ = window.read()
        window.close()

    def get_vaccine(self) -> str:
        layout = [
            [sg.Text('Por favor, insira o nome da vacina:'), sg.InputText(key='vaccine')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Nome da Vacina', layout)
        event, values = window.read()
        window.close()

        return values['vaccine']

    def error_message(self, message: str) -> None:
        layout = [
            [sg.Text(f'Erro: {message}')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Mensagem de Erro', layout)
        event, _ = window.read()
        window.close()

    def get_updated_animal_data(self):
        layout = [
            [sg.Text('Por favor, insira o novo nome do animal:'), sg.InputText(key='name')],
            [sg.Text('Por favor, insira a nova raça do animal:'), sg.InputText(key='breed')],
            [sg.Text('Por favor, insira o novo porte do animal (pequeno|médio|grande):'), sg.InputText(key='size')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Atualizar Informações do Animal', layout)
        event, values = window.read()
        window.close()

        return {
            'name': values['name'],
            'breed': values['breed'],
            'size': values['size']
        }
    
    def get_updated_donor_data(self):
        layout = [
            [sg.Text('Por favor, insira o novo nome do doador:'), sg.InputText(key='name')],
            [sg.Text('Por favor, insira o novo endereço do doador:'), sg.InputText(key='address')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Atualizar Informações do Doador', layout)
        event, values = window.read()
        window.close()

        return {
            'name': values['name'],
            'address': values['address']
        }
    
    def get_all_adopters_view(self, adopters: List[Adopter]) -> None:
        output_text = ""
        for adopter in adopters:
            output_text += f"CPF: {adopter.cpf}\nNome: {adopter.name}\nData de Nascimento: {adopter.birth_date}\nEndereço: {adopter.address}\nTipo de Residência: {adopter.home_type}\nPossui outros pets: {adopter.has_other_pets}\n{'-' * 50}\n"

        layout = [
            [sg.Text('Adotantes Registrados:')],
            [sg.Multiline(output_text, size=(50, len(adopters) * 6), disabled=True)],
            [sg.Button('OK')]
        ]

        window = sg.Window('Adotantes Registrados', layout)
        event, _ = window.read()
        window.close()

    def get_all_donors_view(self, donors: List[Donor]) -> None:
        output_text = ""
        for donor in donors:
            output_text += f"CPF: {donor.cpf}\nNome: {donor.name}\nData de Nascimento: {donor.birth_date}\nEndereço: {donor.address}\n{'-' * 50}\n"

        layout = [
            [sg.Text('Doadores Registrados:')],
            [sg.Multiline(output_text, size=(50, len(donors) * 4), disabled=True)],
            [sg.Button('OK')]
        ]

        window = sg.Window('Doadores Registrados', layout)
        event, _ = window.read()
        window.close()

