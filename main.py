from controller.controller import Controller, MockedView
from repository.person_repo import PersonRepository


controller = Controller(MockedView(), PersonRepository())

controller.start_view()