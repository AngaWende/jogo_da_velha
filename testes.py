p1 = [2,3]

p2 = [3,4]

p3  = [25,97]

lista = [p1,p2,p3]

p0 = (47,2)

def ver_diferença(x,y):
    a = x[0]-y[0]
    b = x[1] - y[1]

    return abs(a+b)
# print(ver_diferença(p3, p1))

resultado = []
for i in lista:
    resultado.append(ver_diferença(i, p0))

print(resultado)
