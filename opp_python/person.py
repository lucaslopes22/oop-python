class Person:
    def __init__(self, name:str, document:str, age:int, height:int):
        self.name = name
        self.__document = document
        self.age = age
        self.height = height


    def setter_document(self, document:str) -> None:
        self.__document = document


    def getter_document(self) -> str:
        return self.__document


    def __show_document(self):
        print(f'Documento: {self.__document}')


    def __str__(self):
        return f'Meu nome é {self.name}, tenho {self.age} anos e tenho {self.height} centímetros de altura'