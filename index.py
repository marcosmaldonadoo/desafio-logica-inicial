import time
import random

nameHero = input("Qual seu nome herói? ")
print("Iremos fazer uma avalição de poder em você, será breve!")
time.sleep(3)
print("Avaliando.......")
time.sleep(4)
levelPower= random.randint(0, 10002)
print("Seu poder é de " + str(levelPower))



if levelPower < 1001: 
    print("O Herói " + nameHero + " está no nível Ferro")
elif levelPower > 1000 and levelPower < 2001:
    print("O Herói " + nameHero + " está no nível Bronze")
elif levelPower > 2001 and levelPower < 3001:
    print("O Herói " + nameHero + " está no nível Prata")
elif levelPower > 3001 and levelPower < 4001:
    print("O Herói " + nameHero + " está no nível Ouro")
elif levelPower > 4001 and levelPower < 5001:
    print("O Herói " + nameHero + " está no nível Diamante")
elif levelPower > 5001 and levelPower < 6001:
    print("O Herói " + nameHero + " está no nível Semi-Deus")
else:
    print("O Herói " + nameHero + " está no nível Imortal")
