import random
import time
jogada_amelia = ['Papel', 'Tesoura', 'Pedra']
print ("""Seja bem vindo ao jokenpô com a Amelia.""")
input ("Aperte ENTER para continuar\n")
inicio = str(input("""Digite Start para iniciar o jogo!\n"""))
inicio = inicio.upper()
inicio = 'SIM'
jogador_perdeu = jogador_ganhou = jogador_empatou = 0

while (inicio == 'START' or inicio == 'SIM'):
    amelia_jogou = random.choice(jogada_amelia)
    amelia_jogou = amelia_jogou.upper()
    jogada = str(input("\nVocê escolhe: Pedra, papel ou tesoura?\n"))
    jogada = jogada.upper()
    if (amelia_jogou==jogada):
        print ("JO...")
        time.sleep(0.75)
        print ("KEN...")
        time.sleep(0.5)
        print("PÔ!")
        time.sleep(0.5)
        print(f"Você jogou {jogada.capitalize()} e Amelia jogou {amelia_jogou.capitalize()}", end=', ')
        time.sleep(1)
        print(f"vocês empataram!")
        jogador_empatou+=1
        inicio = str(input("\n\nDeseja jogar novamente?\nsim/nao\nSua escolha: ")).upper()
        #os.system('cls')
    if (amelia_jogou == 'PEDRA' and jogada == 'TESOURA'):
        print("JO...")
        time.sleep(0.75)
        print("KEN...")
        time.sleep(0.5)
        print("PÔ!")
        time.sleep(0.5)
        print(f"Você jogou {jogada.capitalize()} e Amelia jogou {amelia_jogou.capitalize()}", end = ', ')
        time.sleep(1)
        print (f"você perdeu!")
        time.sleep(2)
        inicio = str(input("\n\nDeseja jogar novamente?\nsim/nao\nSua escolha: ")).upper()
        jogador_perdeu+=1
        #os.system('cls')
    if (amelia_jogou == 'PEDRA' and jogada == 'PAPEL'):
        print("JO...")
        time.sleep(0.75)
        print("KEN...")
        time.sleep(0.5)
        print("PÔ!")
        time.sleep(0.5)
        print(f"Você jogou {jogada.capitalize()} e Amelia jogou {amelia_jogou.capitalize()}", end=', ')
        time.sleep(1)
        print(f"você ganhou!")
        time.sleep(2)
        inicio = str(input("\n\nDeseja jogar novamente?\nsim/nao\nSua escolha: ")).upper()
        jogador_ganhou += 1
        #os.system('cls')
    if (amelia_jogou == 'PAPEL' and jogada == 'TESOURA'):
        print("JO...")
        time.sleep(0.75)
        print("KEN...")
        time.sleep(0.5)
        print("PÔ!")
        time.sleep(0.5)
        print(f"Você jogou {jogada.capitalize()} e Amelia jogou {amelia_jogou.capitalize()}", end=', ')
        time.sleep(1)
        print(f"você ganhou!")
        time.sleep(2)
        inicio = str(input("\n\nDeseja jogar novamente?\nsim/nao\nSua escolha: ")).upper()
        jogador_ganhou += 1
        #os.system('cls')
    if (amelia_jogou == 'PAPEL' and jogada == 'PEDRA'):
        print("JO...")
        time.sleep(0.75)
        print("KEN...")
        time.sleep(0.5)
        print("PÔ!")
        time.sleep(0.5)
        print(f"Você jogou {jogada.capitalize()} e Amelia jogou {amelia_jogou.capitalize()}", end=', ')
        time.sleep(1)
        print(f"você perdeu!")
        time.sleep(2)
        inicio = str(input("\n\nDeseja jogar novamente?\nsim/nao\nSua escolha: ")).upper()
        jogador_perdeu += 1
        #os.system('cls')
    if (amelia_jogou == 'TESOURA' and jogada == 'PAPEL'):
        print("JO...")
        time.sleep(0.75)
        print("KEN...")
        time.sleep(0.5)
        print("PÔ!")
        time.sleep(0.5)
        print(f"Você jogou {jogada.capitalize()} e Amelia jogou {amelia_jogou.capitalize()}", end=', ')
        time.sleep(1)
        print(f"você perdeu!")
        time.sleep(2)
        inicio = str(input("\n\nDeseja jogar novamente?\nsim/nao\nSua escolha: ")).upper()
        jogador_perdeu += 1
        #os.system('cls')
    if (amelia_jogou == 'TESOURA' and jogada == 'PEDRA'):
        print("JO...")
        time.sleep(0.75)
        print("KEN...")
        time.sleep(0.5)
        print("PÔ!")
        time.sleep(0.5)
        print(f"Você jogou {jogada.capitalize()} e Amelia jogou {amelia_jogou.capitalize()}", end=', ')
        time.sleep(1)
        print(f"você ganhou!")
        time.sleep(2)
        inicio = str(input("\n\nDeseja jogar novamente?\nsim/nao\nSua escolha: ")).upper()
        jogador_ganhou += 1
        #os.system('cls')
while (inicio == 'NAO'):
    print (f"Você ganhou {jogador_ganhou} vezes, perdeu {jogador_perdeu} vezes e empatou {jogador_empatou} vezes. Obrigado por jogar!")
    time.sleep(10)
    break