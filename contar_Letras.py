Faça um programa que leia uma String e escreva:
○ O número de letras que a String contém
○ Caractere por caractere, utilizando laço de repetição
○ Caractere por caractere, porém na ordem inversa, utilizando laço de repetição


palavra = input("digite um texto ")
#palavra2 = ""
c = 0
for letras in palavra:
    c += 1
    print(letras)
print(c)

for contrario in range(c-1,-1 , -1):
    print(palavra[contrario])


