import pygame
from time import sleep
from random import randint, choice


pygame.init()

YELLOW = (255, 255, 0)
cor_das_barras = YELLOW
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((420, 420))
# screen = pygame.display.set_mode((1200, 680))
largura = screen.get_width()
altura = screen.get_height()

fonte = pygame.font.SysFont('arial', largura // 19, True)

q1 = (largura // 6, altura // 6)
q2 = (largura // 2, altura // 6)
q3 = (largura // 1.2, altura // 6)
q4 = (largura // 6, altura // 2)
q5 = (largura // 2, altura // 2)
q6 = (largura // 1.2, altura // 2)
q7 = (largura // 6, altura // 1.2)
q8 = (largura // 2, altura // 1.2)
q9 = (largura // 1.2, altura // 1.2)

p_meio = largura // 6

posicoes = [q1, q2, q3, q4, q5, q6, q7, q8, q9]

base_para_X = q1[0] // 3
expessura_padrao = largura // 75

casas_x = []
casas_o = []
jogadas_feitas = []

def resetar():
    global casas_x, casas_o, jogadas_feitas
    casas_x = []
    casas_o = []
    jogadas_feitas = []


def pintar_barras():
    pygame.draw.line(screen, (cor_das_barras), (largura // 3, 0), (largura // 3, altura), expessura_padrao)
    pygame.draw.line(screen, (cor_das_barras), (largura // 1.5, 0), (largura // 1.5, altura), expessura_padrao)
    pygame.draw.line(screen, (cor_das_barras), (0, altura // 3), (largura, altura // 3), expessura_padrao)
    pygame.draw.line(screen, (cor_das_barras), (0, altura // 1.5), (largura, altura // 1.5), expessura_padrao)


def pintar_circulo(pos):
    pygame.draw.circle(screen, BLUE, pos, altura // 7, expessura_padrao)


def pintar_x(pos):
    pygame.draw.line(screen, BLUE, (pos[0] - base_para_X, pos[1] - base_para_X), (pos[0] + 50, pos[1] + base_para_X),
                     expessura_padrao)
    pygame.draw.line(screen, BLUE, (pos[0] - base_para_X, pos[1] + base_para_X), (pos[0] + 50, pos[1] - base_para_X),
                     expessura_padrao)


def validar_vitoria(turno):
    casas = casas_x if turno == 'x' else casas_o
    if (1 in casas and 2 in casas and 3 in casas
            or 1 in casas and 5 in casas and 9 in casas
            or 1 in casas and 4 in casas and 7 in casas
            or 2 in casas and 5 in casas and 8 in casas
            or 3 in casas and 5 in casas and 7 in casas
            or 3 in casas and 6 in casas and 9 in casas
            or 4 in casas and 5 in casas and 6 in casas):
        return True


def tela_final(texto):
    pygame.display.update()
    sleep(0.5)
    img_score = fonte.render(str(texto), True, YELLOW)
    screen.fill(BLACK)
    screen.blit(img_score, (largura // 6, altura // 2))
    pygame.display.update()
    sleep(2)
    print('fim')
    return


def escolha_da_casa(pos):

        if pos[0] < q1[0] + p_meio and pos[1] < q1[1] + p_meio:
            jogada = 1
        elif pos[0] < q2[0] + p_meio and pos[1] < q2[1] + p_meio:
            jogada = 2
        elif pos[0] < q3[0] + p_meio and pos[1] < q3[1] + p_meio:
            jogada = 3
        elif pos[0] < q4[0] + p_meio and pos[1] < q4[1] + p_meio:
            jogada = 4
        elif pos[0] < q5[0] + p_meio and pos[1] < q5[1] + p_meio:
            jogada = 5
        elif pos[0] < q6[0] + p_meio and pos[1] < q6[1] + p_meio:
            jogada = 6
        elif pos[0] < q7[0] + p_meio and pos[1] < q7[1] + p_meio:
            jogada = 7
        elif pos[0] < q8[0] + p_meio and pos[1] < q8[1] + p_meio:
            jogada = 8
        elif pos[0] < q9[0] + p_meio and pos[1] < q9[1] + p_meio:
            jogada = 9


        return jogada



def pintar_casa_turno(jogada,  turno):
    global jogadas_feitas

    if jogada not in jogadas_feitas:
        match jogada:
            case 1:
                pintar_circulo(q1) if turno == 'o' else pintar_x(q1)
            case 2:
                pintar_circulo(q2) if turno == 'o' else pintar_x(q2)
            case 3:
                pintar_circulo(q3) if turno == 'o' else pintar_x(q3)
            case 4:
                pintar_circulo(q4) if turno == 'o' else pintar_x(q4)
            case 5:
                pintar_circulo(q5) if turno == 'o' else pintar_x(q5)
            case 6:
                pintar_circulo(q6) if turno == 'o' else pintar_x(q6)
            case 7:
                pintar_circulo(q7) if turno == 'o' else pintar_x(q7)
            case 8:
                pintar_circulo(q8) if turno == 'o' else pintar_x(q8)
            case 9:
                pintar_circulo(q9) if turno == 'o' else pintar_x(q9)
            case _:
                print('Casa inválida, escolha outra.')
                return False
        jogadas_feitas.append(jogada)
        return True

def encerrar_turno(jogada, turno):
    if pintar_casa_turno(jogada, turno):
        # cont += 1
        if turno == 'x': casas_x.append(jogada)
        if turno == 'o': casas_o.append(jogada)

    pintar_barras()

    print('validando')
    if validar_vitoria(turno):
        print(f'O JOGADOR {turno} VENCEU!!!')
        tela_final(f'O JOGADOR "{turno.upper()}" VENCEU!!!')
        print('xxx')

        return True
        # break

    if len(jogadas_feitas) >= 9:
        tela_final("EMPATE!!!!!")
        return
    print(casas_x, casas_o)

def jogar():
    screen.fill(BLACK)
    pintar_barras()
    cont = 0
    casas_totais = [1,2,3,4,5,6,7,8,9]
    while True:
        # screen.fill(BLACK)
        turno = 'x' if cont % 2 == 0 else 'o'

        jogada_npc = (randint(0, largura), randint(0,altura))
        if turno == 'o':
            sleep(0.5)
            print(casas_totais)
            jogada = choice(casas_totais)
            print(jogada)
            casas_totais.remove(jogada)
            cont+=1
            if encerrar_turno(jogada, turno):
                return turno

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()


            if e.type == pygame.MOUSEBUTTONUP:

                pos = pygame.mouse.get_pos()

                jogada = escolha_da_casa(pos)
                if jogada in casas_totais:
                    casas_totais.remove(jogada)
                    cont += 1
                if encerrar_turno(jogada, turno):
                    return turno

        pygame.display.update()

# jogar()
