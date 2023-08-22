palavra = input("digite um texto ")
c = " "
novo = ""
cont = 0
for letras in palavra:
    if palavra not in c:
        novo = letras + palavra
    cont = cont + 1    
print(f'Esta frase possui {cont} letras')



###########################################
Faça um programa que leia uma frase e imprima o número de palavras que a
frase contém.


palavra = input("digite um texto ")
tam = len(palavra)
i = 0
frase = 0

while i < tam:
    #ignora os espaços em branco
    while i < tam and palavra[i]==" ":
        i += 1
        #verifica se encontrou algo
    if i < tam:
        frase += 1
        #avança até encontrar outro espaço e repete o processo
        while i < tam and palavra[i]!=" ":
            i+=1
print(frase)
