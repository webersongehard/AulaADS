
#faça um algoritmo que receba dez idades, pesos e altura, calcule e mostre:
# a media das idades das dez pessoas; b. a quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,5m
#c a percentagem de pessoas com idade entre 10 e 30 anos que medem mais de 1,9m 
pessoas = 0
peso = float()
n = 0
altura = int()
cont = 0
soma = 0
#while n <= 10:

for pessoas in range(1,4,1):     
    idade = float(input("digite a idade da pessoa: "))
    soma += idade
    peso = float(input("Digite o peso da pessoa:" ))
    #if peso > 90:
    #cont += 1
    altura = float(input("Digite a altura em metros da pessoa: "))
    if peso > 90:
        cont += 1
        if altura < 1.5:
            n += 1
print(f"A média das idades é {soma/3} ")
print(f"A quantidade de pessoas com peso superior a 90 quilos e com tamanho menor que 1.5 é: {n}")

#terminar com a percentagem!
