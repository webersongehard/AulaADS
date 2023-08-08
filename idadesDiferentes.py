''''Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
metro e cresce 3 centímetros por ano. Faça um programa que calcule e
imprima quantos anos serão necessários para que Zé seja maior que Chico.
''''

chico = 150
ze = 110
anos = 0

while ze <= chico:
    ze = ze + 3
    chico = chico + 2
    anos = anos + 1
print(anos)
