x = int(input("Digite por qual número você quer que inicie a contagem: "))
y = int(input("Digite qual o maior número que será mostrado: "))

for contador in range(x,y+1):
    if x < y:
        print(contador)
    else:
        contador in range(y,x,1)
        print(contador)
# não esta finalizado!
