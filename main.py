import pygame
from tela import *
from time import sleep

# pygame.init()
# YELLOW = (255, 255, 0)
# cor_das_barras = YELLOW
# BLACK = (0, 0, 0)
# BLUE = (0, 0, 255)
#
# texto = 'Deseja continuar jogando?'
#
# screen_inicial = pygame.display.set_mode((420, 420))
#
pontos_x = 0
pontos_o = 0

# def pintar_tela_novo_jogo(texto):
#
#     txt_continuar = fonte.render(str(texto), True, YELLOW)
#     sim = fonte.render(str('SIM'), True, YELLOW)
#     nao = fonte.render(str('NÃO'), True, YELLOW)
#     placar_x = fonte.render(str(f'Placar X: {pontos_x}'), True, YELLOW)
#     placar_o = fonte.render(str(f'Placar O: {pontos_o}'), True, YELLOW)
#     screen_inicial.fill(BLACK)
#     screen_inicial.blit(txt_continuar, (largura // 6, altura // 2))
#
#     pygame.draw.line(screen_inicial, BLUE, (q7[0] - 50, q7[1]), (q7[0] + 100, q7[1]), 50)
#     pygame.draw.line(screen_inicial, BLUE, (q9[0] - 100, q9[1]), (q9[0] + 50, q9[1]), 50)
#
#     screen_inicial.blit(sim, (q7[0],q7[1]-10))
#     screen_inicial.blit(nao, (q9[0]-45, q9[1]-10))
#     screen_inicial.blit(placar_x, q1)
#     screen_inicial.blit(placar_o, (q3[0]-100, q3[1]))
#
#     pygame.display.update()
#     # sleep(3)

# jogar()

# while True:
# pintar_tela_novo_jogo(texto)
def iniciar_jogo():
    # pygame.display.update()
    global pontos_x, pontos_o
    while True:
        print(f'X: {pontos_x}')
        print(f'O: {pontos_o}')
        resetar()
        resposta = input("jogar novamente? s/n")

        if resposta == 's':
            somar = jogar()
            match somar:
                case 'x':
                    pontos_x += 1
                case 'o':
                    pontos_o += 1
        else:
            print('saindo')
            break
    # jogar()
    # sleep(5)
    # quit()
iniciar_jogo()



