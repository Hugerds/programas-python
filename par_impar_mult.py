import random
import time
import getpass
import unicodedata
#jogador_1_escolhe
#jogador_2_escolhe
sorteio = random.randint(1,2)
jogador_1_ganhou = jogador_2_perdeu = 0
jogador_1_perdeu = jogador_2_ganhou = 0
reiniciar_jogo = 'SIM'.upper()

print ("BEM VINDO A UM PAR OU ÍMPAR FEITO POR UM MENINO EM NOVATO NISSO!\n\n")
print (f"".center(50, '='))
print (f'Menu Principal'.center(50, '-'))
print (f"".center(50, '='))
print ("\n\n")
while (reiniciar_jogo == 'SIM' or 'S'):
    print ("JOGADOR X JOGADOR\n")
    print ("COMPUTADOR X JOGADOR")
    escolha_player_cpu = str(input("Qual das duas opções? [JJ/JC]\nSua opção: ")).upper()
    if (escolha_player_cpu == 'J' or 'JOGADOR' or 'JOGADORXJOGADOR' or 'JJ'):
        print ("Você escolheu PLAYER X PLAYER\n")
        jogador_1_nome = str(input("Qual o nome do jogador 1?\nNome: ")).capitalize()
        jogador_2_nome = str(input("Qual o nome do jogador 2?\nNome: ")).capitalize()
        print (f"Bem vindos, {jogador_1_nome} e {jogador_2_nome}. Estão prontos?")
        input ("ENTER para continuar")
        print ("Sorteando quem escolherá o lado...")
        time.sleep(1.5)
    if (sorteio==1):
        print(f"O jogador {sorteio} escolherá o lado primeiro.\n\n")
        escolha_lado_jogador_1 = str(input(f"{jogador_1_nome} escolhe PAR ou ÍMPAR?[PAR/IMPAR]\nSua Opção: ")).upper()
        escolha_lado_jogador_1 = unicodedata.normalize('NFKD', escolha_lado_jogador_1).encode('ASCII', 'ignore').decode(
            'ASCII').upper()
        if (escolha_lado_jogador_1 == 'PAR'):
            print(f"\n{jogador_1_nome} escolheu par, {jogador_2_nome} você é ímpar.")
            jogada_jogador_1 = int(input(f"{jogador_1_nome} digite seu número: "))
            jogada_jogador_2 = int(input(f"{jogador_2_nome} digite seu número: "))
            if ((jogada_jogador_1 + jogada_jogador_2) % 2 == 0):
                print(f"{jogador_2_nome} jogou {jogada_jogador_2} e {jogador_1_nome} jogou {jogada_jogador_1}.", end='')
                print(f"{jogador_1_nome} GANHOU!")
        if (escolha_lado_jogador_1 == 'IMPAR'):
            print(f"{jogador_1_nome} escolheu ímpar, {jogador_2_nome} você é par.")
            jogada_jogador_1 = int(input(f"{jogador_1_nome} digite seu número: "))
            jogada_jogador_2 = int(input(f"{jogador_2_nome} digite seu número: "))
            if ((jogada_jogador_1 + jogada_jogador_2) % 2 == 1):
                print(f"{jogador_2_nome} jogou {jogada_jogador_2} e {jogador_1_nome} jogou {jogada_jogador_1}.", end='')
                print(f"{jogador_1_nome} GANHOU!")
            if ((jogada_jogador_1 + jogada_jogador_2) % 2 == 0):
                print(f"{jogador_2_nome} jogou {jogada_jogador_2} e {jogador_1_nome} jogou {jogada_jogador_1}.", end='')
                print(f"{jogador_2_nome} GANHOU!")
    if (sorteio==2):
            print (f"O jogador {sorteio} escolherá o lado primeiro.")
            escolha_lado_jogador_2 = str(input(f"{jogador_2_nome} escolhe PAR ou ÍMPAR?[PAR/IMPAR]\nSua Opção: ")).upper()
            escolha_lado_jogador_2 = unicodedata.normalize('NFKD', escolha_lado_jogador_2).encode('ASCII', 'ignore').decode('ASCII').upper()
            if (escolha_lado_jogador_2 == 'PAR'):
                print (f"{jogador_2_nome} escolheu par, {jogador_1_nome} você é ímpar.")
                jogada_jogador_2 = int(input(f"{jogador_2_nome} digite seu número: "))
                jogada_jogador_1 = int(input(f"{jogador_1_nome} digite seu número: "))
                if ((jogada_jogador_1 + jogada_jogador_2)%2 == 0):
                    print (f"{jogador_1_nome} jogou {jogada_jogador_1} e {jogador_2_nome} jogou {jogada_jogador_2}.", end = '')
                    print (f"{jogador_2_nome} GANHOU!")
            if (escolha_lado_jogador_2 == 'IMPAR'):
                print (f"{jogador_2_nome} escolheu ímpar, {jogador_1_nome} você é par.")
                jogada_jogador_2 = int(input(f"{jogador_2_nome} digite seu número: "))
                jogada_jogador_1 = int(input(f"{jogador_1_nome} digite seu número: "))
                if ((jogada_jogador_1 + jogada_jogador_2)%2 == 1):
                    print (f"{jogador_1_nome} jogou {jogada_jogador_1} e {jogador_2_nome} jogou {jogada_jogador_2}.", end = '')
                    print (f"{jogador_2_nome} GANHOU!")
                    reiniciar_jogo = str(input("\nDeseja reiniciar o programa?[S/N]"))
