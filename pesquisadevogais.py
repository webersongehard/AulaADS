#este programa verifica se existe vogais no texto digitado:

vogais = "aeiou "
texto = "Instituto Federal "
for letra in texto:
    if letra.lower() in vogais:
        print(f'A letra {letra} é uma vogal! ')



###################################################################

texto = input("Digite um testo: ")
vogais = "aeiouAEIOU"
texto_sem_vogais = ""

for letra in texto:
    if(letra not in vogais):
        texto_sem_vogais = texto_sem_vogais + letra

print(texto_sem_vogais)
        
