from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def mostra(slef):
        try:
            print(f"Meu nome é {slef.nome}, tenho {int(slef.idade)} anos e meu email é : {slef.email}")
        except:
            print("escreva um numero para idade ")
idade1 = False
while idade1 is False:
    nome1 = input("qual seu nome ? ")
    email1 = input("qual seu email ? ")
    idade = input("qual seu idade ? ")
    idade1 = idade.isnumeric()
    gui = Cliente(nome1, email1,idade)
    gui.mostra()

