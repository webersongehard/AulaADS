2. Duplas de tênis
Quatro amigos combinaram de jogar tênis em duplas. Cada um dos amigos tem um
nível de jogo, que é representado por um número inteiro: quanto maior o número,
melhor o nível do jogador.
Os quatro amigos querem formar as duplas para iniciar o jogo. De forma a tornar o
jogo mais interessante, eles querem que os níveis dos dois times formados sejam o mais
próximo possível. O nível de um time é a soma dos níveis dos jogadores do time.
Embora eles sejam muito bons jogadores de tênis, os quatro amigos não são muito bons
em algumas outras coisas, como lógica ou matemática. Você pode ajudá-los e encontrar
a menor diferença possível entre os níveis dos times que podem ser formados?
Entrada
A entrada contém quatro linhas, cada linha contendo um inteiro A, B, C e D, indicando
o nível de jogo dos quatro amigos.
Saída
Seu programa deve produzir uma única linha, contendo um único inteiro, a menor
diferença entre os níveis dos dois times formados.
Restrições
• 0 ≤ A ≤ B ≤ C ≤ D ≤ 104


a = int(input("Digite o o nível do jogador A: "))
b = int(input("Digite o o nível do jogador B: "))
c = int(input("Digite o o nível do jogador C: "))
d = int(input("Digite o o nível do jogador D: "))

if 0 <= a <= b <= c <= d <= (10**4):
  print((d+a)-(b+c))
else:
    print("Você digitol valores fora do esperado ")
