PARA COLOCAR O ENUNCIADO DO EXERCICIO NO PYTHON, INSERIR 3 ASPAS SIMPLES ''' E FECHAR COM ELAS.

AP1S1 – Algoritmos e Programação
LISTA 1

1. Faça um programa em Python que leia um número X do usuário e escreva ele na tela no seguinte formato: “O número escolhido foi X”

Num = int(input("O número escolhido foi X"))


2. Faça um programa em Python que leia do usuário dois números. Faça a multiplicação dos dois números e mostre o resultado.

n1 = int(input('Digite a primeiro número'))
n2 = int(input('Digite a segundo número'))
multiplicação = (n1*n2)
print('multiplicação', multiplicação)

3. Faça um programa que leia do usuário um número e escreva o seu sucessor e o seu antecessor.

num = int(input('Digite um número'))
sucessor = (num + 1)
print('sucessor', sucessor)
antecessor = (num - 1)
print('antecessor', antecessor)


4. Faça um programa que leia 2 notas de um aluno, onde a primeira nota possui peso um, a segunda possui peso dois.
Calcule a média ponderada do aluno baseada nos pesos e exiba.

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
média = ((n1*1)+(n2*2))/3
print('média', média)

5. Faça um programa que receba dois inteiros x e y e calcule o valor de z, dado pela expressão a seguir:
 z =(x2+y2) / (x-y)2

x = int(input('valor de x'))
y = int(input('valor de y'))
z = ((x**2)+(y**2))/((y-x)**2)
print('z', z)

6. Faça um programa que receba o salário de um funcionário, reajusta o salário em 25% e
apresenta o valor do reajuste e o novo salário após o aumento.

Salário = float(input('Valor do salário atual'))
Reajustado = (Salário*1.25)
print('Reajustado', Reajustado)

================================================
LISTA 2
1.Faça um programa que receba 5 números inteiros e informe o maior entre eles.

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))
d = int(input("Digite d: "))
e = int(input("Digite e: "))
if a>b and a>c and a>d and a>e:
    print(a)
elif b>a and b>c and b>d and b>e:
    print(b)
elif c>a and c>b and c>d and c>e:
    print(c)
elif d>a and d>b and d>c and d>e:
    print(d)
else:
    print(e)

RESOLUÇÃO: VAMOS CONSIDERAR 5 ENTRADAS DIFERENTES

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: ")))
e = int(input("Digite o quinto valor: "))
if a>b and a>c and a>d and a>e:
    print(f" o maior valor é o {a})
elif b>a and b>c and b>d and b>e:
    print(f" o maior valor é o {b})
elif c>a and c>b and c>d and c>e:
    print(f" o maior valor é o {c})
elif d>a and d>b and d>c and d>e:
    print(f" o maior valor é o {d})
else:
    print(f" o maior valor é o {e})

TESTE DE MESA

__________________________________________________
2. Faça um programa que receba a idade de um eleitor e informa se o voto dele é facultativo (entre 16 e 17 anos),
obrigatório (entre 18 a 65), se ele está dispensado de votar (acima de 65) ou ainda se ele não tem idade para votar.

idade = int(input("Digite sua idade: "))
if idade <16:
    print("não tem idade para votar")
if idade >= 16 and idade <= 17:
    print("votar é facultativo")
if idade >= 18 and idade <= 65:
    print("votar é obrigatório")
else:
    print("dispensado de votar")

RESOLUÇÃO:

idade = int(input("Digite idade do eleitor: "))
if idade >= 16 and idade <18:
    print("voto é facultativo")
if idade >= 18 and idade <= 65:
    print("voto é obrigatório")
else:
    print("dispensado de votar")
____________
NO TESTE DE MESA
SE INSERIR 17, NO TESTE DE MESA
if idade >= 16 and idade <18: SERÁ VERDADE

SE INSERIR 68, NO TESTE DE MESA 68>=16 LE-SE 68>16 OR 68==16.
DÁ VERDADE NA PRIMEIRA E FALSO EM 68==16, NA TABELA VERDADE DO OR, ESSA CONDIÇÃO É VERDADE.
SE INSERIR 24, NO TESTE DE MESA 24>=18 LE-SE 68>18 OR 68==18, NA TABELA VERDADE DO OR, ESSA CONDIÇÃO É VERDADE.
ATÉ 16 E ACIMA DE 65 NÃO VOTAM,  ENTÃO O ELSE INCLUI AMBAS.
_______________________________________________________________________________
3. Escreva um programa que leia três números inteiros e os imprima em ordem crescente.

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))
if a>=b and a>c and b>=c:
    print(a, b, c)
elif a>b and a>=c and c>b:
    print(a, c, b)
elif b>a and b>c and a>=c:
    print(b, a, c)
elif b>a and b>=c and c>a:
    print(b, c, a)
elif c>a and c>b and a>=b:
    print(c, a, b)
elif c>a and c>b and b>a:
    print(c, b, a)
else:
    print("são todos iguais")

RESOLUÇÃO
n1 = int(input("digite o primeiro valor: "))
n2 = int(input("digite o segundo valor: "))
n3 = int(input("digite o terceiro valor: "))
if n1<n2 and n1<n3:
	if n2<n3:
		print(f"ordem crescente: {n1}{n2}{n3})
	else:
		print(f"ordem crescente: {n1}{n3}{n2})

if n2<n1 and n2<n3:
	if n1<n3:
		print(f"ordem crescente: {n2} {n1}{n3})
	else:
		print(f"ordem crescente: {n2}{n3}{n1})

if n3<n1 and n3<n2:
if n1<n2:
  print(f"ordem crescente: {n3} {n1}{n2})
else:
print(f"ordem crescente: {n3}{n2}{n1})

NO TESTE DE MESA
CONSIDERANDO N1 7, N2 82 E N3 84, SERÁ VERDADE NO PRIMEIRO if n1<n2 and n1<n3 and n2<n3
CONSIDERANDO N1 82, N2 94 E N3 82, SERÁ VERDADE NO SEGUNDO if n1<n2 and n1<n3 and n2<n3
CONSIDERANDO N1 94, N2 82 E N3 7, SERÁ VERDADE NO SEGUNDO if n1<n2 and n1<n3 and n2<n3
__________________________________________________
4. Faça um algoritmo que receba três valores A, B e C e verifica se eles podem ser os comprimentos dos lados de um triângulo.
Se forem, mostrar se é um triângulo equilátero, isósceles ou escaleno. Considere que: 
Para ser triângulo: cada lado é menor que a soma dos outros dois lados. 
Triângulo equilátero: tem três lados iguais  Triângulo isósceles: tem dois lados iguais e um diferente 
Triângulo escaleno: tem três lados diferentes

A = int(input("Digite um numero A: "))
B = int(input("Digite um numero B: "))
C = int(input("Digite um numero C: "))
if A+B >C and A+C > B and C+B >A:
    print("é triangulo")
elif A == B and  == C:
    print("triangulo equilátero")
elif A == B !=C and A == C !=B and C == B !=A:
    print("triangulo isóceles")
elif A!=B and A != C and B!=C and A!=0 and B!= 0 and C!=0 :
    print("triangulo escaleno")
else: # não é triangulo!
    print("não é triangulo")

RESOLUCAO
A = int(input("Digite o valor do primeiro lado: "))
B = int(input("Digite o valor do segundo lado: "))
C = int(input("Digite o valor do terceiro lado: "))
if A<B+C and B<A+C and C<A+B:
if A==B and B==C:
print ("triângulo equilátero.")
elif A==B or A==C or B==C:
print("triângulo isóceles")
else:
print("triângulo escaleno")
else:

print("não é triângulo")




_____________________________________________________
5. Crie um algoritmo para resolver equações do 2º grau.
Considere: ax2 + bx+ c = 0  (a deve ser diferente de 0) delta = b2 -4 * a * c
• delta < 0, não existe raiz real
• delta = 0, existe uma raiz real:  x = (-b) / (2 * a)
• delta > 0, existem duas raízes reais: x1 = (-b + raiz quadrada de delta) / (2 * a) ; x2 = (-b -raiz quadrada de delta) / (2 * a)

1,1,1 ( não tem raiz)
1,2,1 (-1)
1,0,-4 (2,-2)
# resolver ax2+bx+c=0

a = int(input("Informe um valor para a diferente de zero "))  
b = int(input("Valor de b "))
c = int(input("Valor de c "))
delta=(b**2)-(4*a*c)
x = -b / (2 * a)
x1 = (-b + delta**(1/2)) / (2 * a)
x2 = (-b - delta**(1/2)) / (2 * a)
	print("Cálculo do delta", delta)
if delta<0:
    print("Valor de delta menor que 0, então não existe raiz real", delta)
elif delta==0:
    print ('Valor de delta igual a zero, existe uma raiz real', x)
elif delta>0:
    print ('Valor de delta maior que 0, existem duas raizes reais',x1,x2)
__________________
RESOLUÇÃO

import math #para calcular a raiz quadrada é necessário usar a biblioteca matemática - para saber qual função segure o ctrl e clique em qualquer parte.
a = int(input("Informe um valor para a"))
if a==0:
	print("o valor de a não pode ser zero")
else:
	b=int(input("entre com o valor de b:"))
	c=int(input("entre com o valor de c:"))
	delta=(b**2)-4*a*c
	if delta < 0:
		print("não existe raiz real.")
	elif delta==0:
		x = -b / (2 * a)
		print(f" existe raiz real: {x}")
	else:
		x1 = (-b + math.sqrt(delta)) / (2 * a) # math.sqrt()calcula 
		x2 = (-b - math.sqrt(delta)) / (2 * a)
		print("existe duas raízes reais:")
		print(f" raiz 1: {x1} raiz 1: {x2}")
_____________________________________________________

6. Uma determinada loja está fazendo promoções de vendas. Qualquer compra que um cliente fizer até R$ 100,00 receberá 5% de desconto. Se a compra for maior que R$ 100,00, mas inferior a R$ 200,00, o desconto será de 10%. Se for superior ou igual a R$ 200,00, o desconto será de 20%. Faça um programa que leia o quanto o cliente gastou e escreva o valor da conta já com os descontos.

a = int(input("Valor da compra: "))
b= a*0.95 #se a<=100
c= a*0.9 #se a>100 and a<200
d= a*0.8 #se a>=200
if a<=100:
    print("novo valor com desconto de 5%", b)
elif a>100 and a<200:
    print("desconto de 10%",c)
elif a>=200:
    print("desconto de 20%",d)

________
RESOLUCAO

valor_gasto=float(input("entre com o valor total gasto:"))
if valor_gasto > 100 and valor_gasto < 200:
	print("valor desconto:", valor_gasto * 0.9)
elif valor_gasto >=200:
	print("valor desconto:", valor_gasto * 0.8)
else:
	print("valor desconto:", valor_gasto * 0.95)

=================================


'''estrutura de repetição while - FORÇA O USUÁRIO ATÉ DAR UMA CONDIÇÃO VÁLIDA. O USUARIO PODE INSERIR INFINITAS VEZES, OU SEJA, LOOPING. 
PARA DAR FIM A REPETIÇAO
se contrói: 
while condição:
    <bloco de comandos a ser executado enquanto a condição for verdadeira>'''
EXEMPLO EXERCICIO 5

import math #para calcular a raiz quadrada é necessário usar a biblioteca matemática - para saber qual função segure o ctrl e clique em qualquer parte.

a = int(input("Informe um valor para a"))
while a==0:
	print("entre com o novo valor de a")
else:
b=int(input("entre com o valor de b:"))
c=int(input("entre com o valor de c:"))
delta=(b**2)-4*a*c
if delta < 0:
	print("não existe raiz real.")
elif delta==0:
	x = -b / (2 * a)
	print(f" existe raiz real: {x}")
else:
	x1 = (-b + math.sqrt(delta)) / (2 * a) # math.sqrt()calcula 
	x2 = (-b - math.sqrt(delta)) / (2 * a)
	print("existe duas raízes reais:")
	print(f" raiz 1: {x1} raiz 1: {x2}")
	
	






