import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_AO.UTF-8')
os.system("CLS")
while True:
   
        num1 = input("Escreva um numero: ").replace(",",".")

        
        
        oper = input("Escreva o simbulo do aperador que voce quer + ou - ou * ou / :")

        num2 = input("Escreva outro numero: ").replace(",",".") 
        num = None

        try:
            num1 = float(num1)
            num2 = float(num2)
            num = True
            if oper is "+":
                 print(f"a soma dos numeros é {num1+num2}")
            elif oper is "-":
                 print(f"A subitraçao dos numero é {num1-num2}")
            elif oper is "*":
                 print(f"A multipicçao dos numeros é {num1 * num2}")
            elif oper is "/":
                 print(f"A diviao dos numeros é {num1/num2}")
            else:
                 print("nem um simbolos corespondetes ") 
            cont = input("voce quer continuar escreva n para que qualquer outra telcla para sim ").lower().startswith() 
            if cont is True:
                 print("Adeus ")
                 break  
        except:
            if num is None:
                  print("o numero 1 ou 2 nao é um numero ")
            else:
                print("qual quer outro erro achado ")


       
           
            
        
       
       