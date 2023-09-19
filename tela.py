import pygame
from time import sleep

pygame.init()

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((420,420))
# screen = pygame.display.set_mode((1200, 680))
largura = screen.get_width()
altura = screen.get_height()

p1 = (largura // 6, altura//6)
p2 = (largura // 2, altura//6)
p3 = (largura // 1.2, altura//6)
p4 = (largura // 6, altura//2)
p5 = (largura // 2, altura//2)
p6 = (largura // 1.2, altura//2)
p7 = (largura // 6, altura//1.2)
p8 = (largura // 2, altura//1.2)
p9 = (largura // 1.2, altura//1.2)

p_meio = largura // 6

posicoes = [p1, p2,p3,p4,p5,p6,p7,p8,p9]

base_para_X = p1[0] // 3
expessura_padrao = largura // 75

def pintar_circulo(pos):
    pygame.draw.circle(screen, BLUE, pos, altura // 7, expessura_padrao)

def pintar_x(pos):
    pygame.draw.line(screen, BLUE, (pos[0] - base_para_X, pos[1] - base_para_X), (pos[0] + 50, pos[1] + base_para_X), expessura_padrao)
    pygame.draw.line(screen, BLUE, (pos[0]-base_para_X, pos[1]+base_para_X), (pos[0]+50, pos[1]-base_para_X), expessura_padrao)


cont = 0

while True:
    # screen.fill(BLACK)
    turno = 'x' if cont % 2 == 0 else 'o'
    r1 = pygame.draw.line(screen, (YELLOW), (largura //3, 0 ), (largura//3,altura), expessura_padrao)
    r2 = pygame.draw.line(screen, (YELLOW), (largura //1.5, 0 ), (largura//1.5,altura), expessura_padrao)
    r3 = pygame.draw.line(screen, (YELLOW), (0, altura//3), (largura, altura//3), expessura_padrao)
    r4 = pygame.draw.line(screen, (YELLOW), (0, altura//1.5), (largura, altura//1.5),expessura_padrao)




    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.MOUSEBUTTONUP:
            cont += 1
            print('ojoij')
            pos = pygame.mouse.get_pos()
            print(cont)

            if pos[0] < p1[0]+p_meio and pos[1]<p1[1]+p_meio:
                pintar_circulo(p1) if turno == 'o' else pintar_x(p1)
            elif pos[0] < p2[0]+p_meio  and pos[1]<p2[1]+p_meio:
                pintar_circulo(p2) if turno == 'o' else pintar_x(p2)
            elif pos[0] < p3[0] +p_meio and pos[1] < p3[1]+p_meio:
                pintar_circulo(p3) if turno == 'o' else pintar_x(p3)
            elif pos[0] < p4[0]+p_meio and pos[1]<p4[1]+p_meio:
                pintar_circulo(p4) if turno == 'o' else pintar_x(p4)
            elif pos[0] < p5[0]+p_meio and pos[1]<p5[1]+p_meio:
                pintar_circulo(p5) if turno == 'o' else pintar_x(p5)
            elif pos[0] < p6[0]+p_meio and pos[1]<p6[1]+p_meio:
                pintar_circulo(p6) if turno == 'o' else pintar_x(p6)
            elif pos[0] < p7[0]+p_meio and pos[1]<p7[1]+p_meio:
                pintar_circulo(p7) if turno == 'o' else pintar_x(p7)
            elif pos[0] < p8[0]+p_meio and pos[1]<p8[1]+p_meio:
                pintar_circulo(p8) if turno == 'o' else pintar_x(p8)
            elif pos[0] < p9[0]+p_meio and pos[1]<p9[1]+p_meio:
                pintar_circulo(p9) if turno == 'o' else pintar_x(p9)





    pygame.display.update()




