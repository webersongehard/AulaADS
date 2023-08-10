#Faça um programa que leia um conjunto de valores positivos maiores que zero.
#Quando for fornecido um número negativo, deve-se terminar a leitura. Ao fim,
#seu programa deve imprimir o maior valor lido.

n = int(input("Digite um número: "))
i = 1
maior = 0
while n >= 0 :
    if n == 0:
        print("Voce digitou 0: ")
    n = int(input("Digite um número: "))
    i = i + 1
    if i == 1:
        maior = n
    else:
        if n > maior:
            maior = n
    
print(f" O maior número digitado foi: {maior} ")
