#este programa verifica se existe vogais no texto digitado:

vogais = "aeiou "
texto = "Instituto Federal "
for letra in texto:
    if letra.lower() in vogais:
        print(f'A letra {letra} é uma vogal! ')
