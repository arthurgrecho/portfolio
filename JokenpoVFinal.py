import random
pont = 0
pont2 = 0

cont = ''
menu = int(input('Selecione o modo de jogo: JogadorxJogador (7) JogadorxComputador (8) ComputadorxComputador (9) ou (0) para Sair'))
if menu == 0:
    print('Você saiu do jogo!')
    print('Feito por: Yan Marco Ferreira Gelbcke, André Luís Scharaiber Alves, Bruno Antunes e Arthur Grechoniak')

elif menu == 8 :
    print('O modo Jogador contra CPU foi escolhido')
    while True :
        y = int(input('Digite um valor: (1) para Pedra (2) para Papel (3) para Tesoura'))
        if y == 1 :
          print('Você escolheu Pedra')
        elif y == 2 :
            print('Você escolheu Papel')
        elif y == 3 :
            print('Você escolheu Tesoura')
        elif y > 3 or y < 1 :
          print('Você escolheu um número inválido, favor digitar um número válido')

        x = random.randint(1, 3)
        if x == 1 :
            print('O Computador escolheu Pedra')
        elif x == 2 :
            print('O Computador escolheu Papel')
        elif x == 3 :
            print('O Computador escolheu Tesoura')

        if x == 3 and y == 1:
            pont = pont + 1
            print('O Jogador venceu')
            print("Humano: " + str(pont))
            print("Computador: " + str(pont2))

        elif y == 3 and x == 1:
            pont2 = pont2 + 1
            print('O Computador venceu')
            print("Humano: " + str(pont))
            print("Computador: " + str(pont2))

        elif x > y :
            pont2 = pont2 + 1
            print('O Computador venceu')
            print("Humano: " + str(pont))
            print("Computador: " + str(pont2))

        elif y > x :
            pont = pont + 1
            print('O Jogador venceu')
            print("Humano: " + str(pont))
            print("Computador: " + str(pont2))

        elif x == y :
            print('Ocorreu um empate')
            print("Humano: " + str(pont))
            print("Computador: " + str(pont2))

        while True:
            cont = str(input('Você deseja jogar novamente? [S/N]')).strip().upper()[0]
            if cont not in 'SN':
                print('Digite um valor válido')
            else :
                break
        if cont == 'N':
            print('Você saiu do jogo, obrigado por jogar! Pontuação Final: ')
            print("Humano: " + str(pont))
            print("Computador: " + str(pont2))
            print('Feito por: Yan Marco Ferreira Gelbcke, André Luís Scharaiber Alves, Bruno Antunes e Arthur Grechoniak')
            break

elif menu == 9 :
    print('Você escolheu Computador contra Computador')
    while True :

        a = (random.randint(1, 3))
        b = (random.randint(1, 3))
        if a == 1 and b == 1:
            print("cpu1 = pedra VS cpu2 = pedra")
            print("Ocorreu um empate!")
            print("Computador 1: " + str(pont))
            print("Computador2: " + str(pont2))

        elif a == 1 and b == 2:
            pont2 = pont2 + 1
            print("cpu1 = pedra VS cpu2 = papel")
            print("O Computador 2 - Ganhou!")
            print("Computador 1: " + str(pont))
            print("Computador 2: " + str(pont2))

        elif a == 1 and b == 3:
            pont = pont + 1
            print("cpu1 = pedra VS cpu2 = tesoura")
            print("O Computador 1 - Ganhou!")
            print("Computador 1: " + str(pont))
            print("Computador 2: " + str(pont2))

        elif a == 2 and b == 1:
            pont = pont + 1
            print("cpu1 = papel VS cpu2 = pedra")
            print("O Computador 1 - Ganhou!")
            print("Computador 1: " + str(pont))
            print("Computador 2: " + str(pont2))

        elif a == 2 and b == 2:
            print("cpu1 = papel VS cpu2 = papel")
            print("Ocorreu um empate!")
            print("Computador 1: " + str(pont))
            print("Computador 2: " + str(pont2))

        elif a == 2 and b == 3:
            pont2 = pont2 + 1
            print("cpu1 = papel VS cpu2 = tesoura")
            print("O Computador 2 - Ganhou!")
            print("Computador 1: " + str(pont))
            print("Computador 2: " + str(pont2))

        elif a == 3 and b == 1:
            pont2 = pont2 + 1
            print("cpu1 = tesoura VS cpu2 = pedra")
            print("O Computador 2 - Ganhou!")
            print("Computador 1: " + str(pont))
            print("Computador 2: " + str(pont2))

        elif a == 3 and b == 2:
            pont = pont + 1
            print("cpu1 = tesoura VS cpu2 = papel")
            print("O Computador 1 ganhou!")
            print("Computador 1: " + str(pont))
            print("Computador 2: " + str(pont2))

        elif a == 3 and b == 3:
            print("cpu1 = tesoura VS cpu2 = tesoura")
            print("Ocorreu um empate!")
            print("Computador 1: " + str(pont))
            print("Computador 2: " + str(pont2))

        while True:
            cont = str(input('Você deseja jogar novamente? [S/N]')).strip().upper()[0]
            if cont not in 'SN':
                print('Digite um valor válido')
            else:
                break
        if cont == 'N':
            print('Você saiu do jogo, obrigado por jogar! Pontuação Final: ')
            print("Computador 1: " + str(pont))
            print("Computador 2: " + str(pont2))
            print('Feito por: Yan Marco Ferreira Gelbcke, André Luís Scharaiber Alves, Bruno Antunes e Arthur Grechoniak')
            break

elif menu == 7 :
    print('Você escolheu o modo jogador contra jogador')
    while True :
        print("Escolha (1) para pedra, (2) para papel ou (3) para tesoura.")

        x = int(input("Jogador 1, selecione sua escolha: "))
        y = int(input("Jogador 2, selecione sua escolha: "))

        if x == 1 and y == 1:
            print("Jogador 1 escolheu pedra VS Jogador 2 escolheu pedra")
            print("Ocorreu um empate!")
            print("Jogador 1: " + str(pont))
            print("Jogador 2: " + str(pont2))


        elif x == 1 and y == 2:
            pont2 = pont2 + 1
            print("Jogador 1 escolheu pedra VS Jogador 2 escolheu papel")
            print("O jogador 2 - Ganhou!")
            print("Jogador 1: " + str(pont))
            print("Jogador 2: " + str(pont2))


        elif x == 1 and y == 3:
            pont = pont + 1
            print("Jogador 1 escolheu pedra VS Jogador 2 escolheu tesoura")
            print("O jogador 1 - Ganhou!")
            print("Jogador 1: " + str(pont))
            print("Jogador 2: " + str(pont2))


        elif x == 2 and y == 1:
            pont = pont + 1
            print("Jogador 1 escolheu papel VS Jogador 2 escolheu pedra")
            print("O jogador 1 - Ganhou!")
            print("Jogador 1: " + str(pont))
            print("Jogador 2: " + str(pont2))


        elif x == 2 and y == 2:
            print("Jogador 1 escolheu papel VS Jogador 2 escolheu = papel")
            print("Ocorreu um empate!")
            print("Jogador 1: " + str(pont))
            print("Jogador 2: " + str(pont2))


        elif x == 2 and y == 3:
            pont2 = pont2 + 1
            print("Jogador 1 escolheu papel VS Jogador 2 escolheu tesoura")
            print("O jogador 2 - Ganhou!")
            print("Jogador 1: " + str(pont))
            print("Jogador 2: " + str(pont2))


        elif x == 3 and y == 1:
            pont2 = pont2 + 1
            print("Jogador 1 escolheu tesoura VS Jogador 2 escolheu pedra")
            print("O jogador 2 - Ganhou!")
            print("Jogador 1: " + str(pont))
            print("Jogador 2: " + str(pont2))


        elif x == 3 and y == 2:
            pont = pont + 1
            print("Jogador 1 escolheu tesoura VS Jogador 2 escolheu = papel")
            print("O jogador 1 - Ganhou!")
            print("Jogador 1: " + str(pont))
            print("Jogador 2: " + str(pont2))


        elif x == 3 and y == 3:
            print("Jogador 1 escolheu tesoura VS Jogador 2 escolheu tesoura")
            print("Ocorreu um empate!")
            print("Jogador 1: " + str(pont))
            print("Jogador 2: " + str(pont2))

        while True:
            cont = str(input('Você deseja jogar novamente? [S/N]')).strip().upper()[0]
            if cont not in 'SN':
                print('Digite um valor válido')
            else:
                break
        if cont == 'N':
            print('Você saiu do jogo, obrigado por jogar! Pontuação Final: ')
            print("Jogador 1: " + str(pont))
            print("Jogador 2: " + str(pont2))
            print('Feito por: Yan Marco Ferreira Gelbcke, André Luís Scharaiber Alves, Bruno Antunes e Arthur Grechoniak')
            break