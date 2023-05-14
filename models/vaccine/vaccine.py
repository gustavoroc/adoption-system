class Vaccine:
    def __init__(self, name: str, date_of_application: str):
        self.__name = name
        self.__date_of_application = date_of_application

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def date_of_application(self):
        return self.__date_of_application
    
    @date_of_application.setter
    def date_of_application(self, value):
        self.__date_of_application = value