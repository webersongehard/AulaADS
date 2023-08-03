a = int(input("Digite o o nível do jogador A: "))
b = int(input("Digite o o nível do jogador B: "))
c = int(input("Digite o o nível do jogador C: "))
d = int(input("Digite o o nível do jogador D: "))

if a <= b <= c <= d <= (10**2):
    if a == b and c < d :
        print(d+a - c+b)
    
