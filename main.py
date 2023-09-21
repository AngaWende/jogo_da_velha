import pygame
from tela import *
from time import sleep

pygame.init()
YELLOW = (255, 255, 0)
cor_das_barras = YELLOW
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

texto = 'Deseja continuar jogando?'

screen_inicial = pygame.display.set_mode((420, 420))
#
pontos_x = 0
pontos_o = 0

def pintar_score():

    placar_x = fonte.render(str(f'Placar X: {pontos_x}'), True, YELLOW)
    placar_o = fonte.render(str(f'Placar O: {pontos_o}'), True, YELLOW)
    screen_inicial.blit(placar_x, q1)
    screen_inicial.blit(placar_o, (q3[0] - 100, q3[1]))

def pintar_tela_novo_jogo(texto):
    global pontos_o, pontos_x

    txt_continuar = fonte.render(str(texto), True, YELLOW)
    sim = fonte.render(str('SIM'), True, YELLOW)
    nao = fonte.render(str('NÃO'), True, YELLOW)
    # screen_inicial.fill(BLACK)
    # screen_inicial.blit(txt_continuar, (largura // 6, altura // 2))
    pos_botao_sim = (q7[0], q7[1] - 10)
    pos_botao_nao = (q9[0] - 45, q9[1] - 10)

    while True:
        screen_inicial.fill(BLACK)
        screen_inicial.blit(txt_continuar, (largura // 6, altura // 2))
        pygame.draw.line(screen_inicial, BLUE, (q7[0] - 50, q7[1]), (q7[0] + 100, q7[1]), 50)
        pygame.draw.line(screen_inicial, BLUE, (q9[0] - 100, q9[1]), (q9[0] + 50, q9[1]), 50)

        screen_inicial.blit(sim, pos_botao_sim )
        screen_inicial.blit(nao, pos_botao_nao)

        pintar_score()
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                print(pos)
                print(pos_botao_sim)
                if  pos[0] > pos_botao_sim[0] - 50  and pos[0] < pos_botao_sim[0] +105  and pos[1] < pos_botao_sim[1] + 40 and pos[1] > pos_botao_sim[1]-13 :
                    print('sim')
                    # pontos_x += 1
                    return 'sim'
                elif pos[0] > pos_botao_nao[0] - 53 and pos[0] < pos_botao_nao[0] + 97 and pos[1] < pos_botao_nao[1] + 40 and pos[1] > pos_botao_nao[1]-13:
                    print('não')
                    print(pontos_o)
                    # pontos_o += 1
                    return 'não'




# somar = jogar()
# match somar:
#     case 'x':
#         pontos_x += 1
#     case 'o':
#         pontos_o += 1


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

if __name__=='__main__':
    somar = jogar()
    match somar:
        case 'x':
            pontos_x += 1
        case 'o':
            pontos_o += 1
    # iniciar_jogo()
    while True:
        print('entrou no while')
        resposta = pintar_tela_novo_jogo(texto)
        if resposta == 'sim':
            resetar()
            somar = jogar()
            match somar:
                case 'x':
                    pontos_x += 1
                case 'o':
                    pontos_o += 1
        elif resposta  == 'não':
            quit()



