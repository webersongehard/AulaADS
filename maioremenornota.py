#Ler um conjunto de valores correspondentes às notas que alunos obtiveram
#em uma prova. Quando o valor fornecido for um número negativo, significa
#que não existem mais pontos para serem lidos.
#○ Escrever o número de alunos
#○ Escrever a maior nota
#○ Escrever a menor nota

alunos = int(input("Digite quantos alunos fizeram a prova: "))
nota = float(input("Qual foi a nota tirada: "))
n = 0

while n <= alunos:
    if nota >= 0:
        nota = float(input("Qual foi a nota tirada: "))
