texto = "algoritmos e programação"
textonovo = texto.upper()
print(textonovo)




####################################################


texto1 = "minúsculas"
texto2 = "MAIÚSCULAS"
#textonovo = texto.upper()
print(texto1.islower())
print(texto1.isupper())
print(texto2.islower())
print(texto2.isupper())

saida:
True
False
False
True



####################################################

entrada = '54987'
if entrada.isdigit():
    print('A entrada corresponde ao numero', int(entrada))
else:
    print('A entrada é um texto')

saida:
A entrada corresponde ao numero 54987
