import random

def rodaDado():
    num = random.randint(1,6)
    print(f"O número do dado é {num}")


resp = str(input("Você deseja jogar o dado?\nSim/Não\nSua opção: "))
if "sim" or "SIM" or "s" in resp:
    rodaDado()
if "não" or "nao" or "n" or "NÃO" or "NAO" in resp:
    print ("Obrigado por usar o programa!")
    quit()