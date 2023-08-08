# série harmonica

h = int(input("Digite um número para ver a sua soma harmonica "))

i = 1
soma = 0

while i <= h :
    soma = soma + 1/i
    i += 1

print(f"A soma harmonica dos n termos é {soma}")
