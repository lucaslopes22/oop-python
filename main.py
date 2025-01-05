from opp_python.person import Person
from opp_python.cadastral_system import CadastralSystem

if __name__ == '__main__':
    person = Person('Luke','11111111111', 18, 190)
    cadastral_system = CadastralSystem(person)
    cadastral_system.register()