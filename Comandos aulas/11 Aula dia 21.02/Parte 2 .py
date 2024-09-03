import random as ra
import os
os.system("cls")
nomes_lista = [ 
    "FELIPE ANTUNES GONCALVES", "GABRIEL DE DEUS LOPES",   
    "GABRIEL HENRIQUE DE OLIVEIRA", "GUSTAVO CORREA SOUZA", 
    "GUSTAVO HENRIQUE TEIXEIRA DA SILVA", "HELLEN CRISTINA PEREIRA ROCHA", "HIGOR ESTEVAO DE SOUZA GONCALVES", 
    "IAGO BRIAN DE OLIVEIRA SANTANA",
    "ITALO HENRIQUE BERALDO DA SILVA"," JOAO FELIPE DE OLIVEIRA NASCIMENTO"," JOÃO PEDRO ALMEIDA MOREIRA", 
    "KAUAN GABRIEL ANDRADE COSTA", "LUANA GONCALVES GUIMARAES DE CASTRO", "MATHEUS FILIPE ALVES GOMES", 
    "OTAVIO HENRIQUE MARQUES DA SILVA GREGORIO", "PEDRO HENRIQUE MENDES OLIVEIRA", 
    "PEDRO HENRIQUE SILVA CANDIDO","RENAN LUCAS VILETE ","RICASSIO"
    "BRUNO GONCALVES DA SILVA",  
    "SAMUEL MACIEL DA SILVA FIGUEIREDO"," TIAGO RAMOS DA SILVA", 
    "VITOR HENRIQUE DOS SANTOS", "ALBERTO BATISTA CUSTODIO OLIVEIRA COSTA","Dudu"]

sorte= ra.randint(1,3)
sorte_aluno = ra.randint(0,24)
if sorte is 1:
   print(f"O aluno {nomes_lista[sorte_aluno]} vai cair da escada de 4 degrais")
elif sorte is 2:
    print(f"O aluno {nomes_lista[sorte_aluno]} vai assumir que é gay")
else:
   print(f"O aluno {nomes_lista[sorte_aluno]} vai sumir com todo o dinheiro da familha ")
