# verificando um número digitado se ele é par ou ímpar

x = int(input("Digite um número qualquer: "))

while (x != 0):

    if (x % 2 == 0):
        print(f"O número {x} é par! ")

    else:
         print(f"O número {x} é ímpar! ")
        
    x = int(input("Digite um número qualquer: "))        
  
print("** Fim da execução **")
