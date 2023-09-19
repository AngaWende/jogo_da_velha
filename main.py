p1 = '_'
p2 = '_'
p3 = '_'
p4 = '_'
p5 = '_'
p6 = '_'
p7 = ' '
p8 = ' '
p9 = ' '


def print_tab():
    print(f'''{p1}|{p2}|{p3}         1|2|3    
{p4}|{p5}|{p6}         4|5|6
{p7}|{p8}|{p9}         7|8|9
''')

def validar_vitoria(turno):
    casas = casas_x if turno == 'X' else casas_o
    if (1 in casas and 2 in casas and 3 in casas
            or 1 in casas and 5 in casas and 9 in casas
            or 1 in casas and 4 in casas and 7 in casas
            or 2 in casas and 5 in casas and 8 in casas
            or 3 in casas and 5 in casas and 7 in casas
            or 3 in casas and 6 in casas and 9 in casas
            or 4 in casas and 5 in casas and 6 in casas):
        return True



casas_x = []
casas_o = []

print_tab()

contador = 0
jogadas_feitas = []
while True:
    turno = 'X' if contador % 2 == 0 else 'O'
    jogada = input(f'Digite a posição do "{turno}": ')


    if jogada not in jogadas_feitas:
        match jogada:
            case '1': p1 = turno
            case '2': p2 = turno
            case '3': p3 = turno
            case '4': p4 = turno
            case '5': p5 = turno
            case '6': p6 = turno
            case '7': p7 = turno
            case '8': p8 = turno
            case '9': p9 = turno
            case _:
                print('Casa inválida, escolha outra.')
                continue
        jogadas_feitas.append(jogada)
    else:
        print('Casa ocupada, escolha outra.')
        continue

    if turno =='X': casas_x.append(int(jogada))
    if turno =='O': casas_o.append(int(jogada))

    print_tab()
    print(f'x = {casas_x}')
    print(f'o = {casas_o}')
    if validar_vitoria(turno):
        print(f'O JOGADOR {turno} VENCEU!!!')
        break
    contador += 1
    if contador >=9:
        print("EMPATE!!!!!")
        break

