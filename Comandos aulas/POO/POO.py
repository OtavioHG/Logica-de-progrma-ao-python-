class Aluno:
    def __init__(self,nome,cadastro):
        try:
            self.nome = nome
            self.cadastro = int(cadastro)
        except:
            print("Por favor escreva um numero")

    def mostra(slef):
        try:
            print(slef.nome,slef.cadastro)
        except:
            print(slef.nome)

n1 = input("Qual seu nome ? ")
c1 = input("Qual seu cadastro ? ")

aluno1 = Aluno(n1,c1)

aluno1.mostra()

        