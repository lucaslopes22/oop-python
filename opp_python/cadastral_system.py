from opp_python.person import Person

class CadastralSystem:
    """
    Essa classe tem por objetivo demonstrar o que é o S do SOLID

    #### Exemplo de código que fere o SRP:

    ```python
    class CadastralSystem:
        def register(self, name: str, age: int) -> None:
            if isinstance(name, str) and isinstance(age, int):
                print("Acessando o banco de  dados...")
                print(f"Cadastrar usuário {name}, idade {age}")
            else:
                print("Dados inválidos")
    ```
    """

    def __init__(self, person: Person):
        self.__person = person


    def register(self) -> None:
        if self.__validate_input(self.__person.name, self.__person.age):
            self.__register_user(self.__person.name, self.__person.age)
        else:
            self.__error_handle()


    def __validate_input(self, name: str, age: int) -> bool:
        return isinstance(name, str) and isinstance(age, int)


    def __register_user(self, name: str, age: int) -> None:
        print("Acessando o banco de  dados...")
        print(f"Cadastrar usuário {name}, idade {age}")


    def __error_handle(self) -> None:
        print('Dados inválidos')