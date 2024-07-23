import math

def bhas(a, b, c):
    delta = (b**2) - (4*a*c)
    d = 2*a
    
    if delta < 0 or d == 0:
        return print('Impossivel calcular')
    
    delta = math.sqrt(delta)

    x1 = (-b + delta)/(2*a)
    x2 = (-b - delta)/(2*a)
    return print(f'R1 = {x1:.5f}\nR2 = {x2:.5f}')


a, b, c = map(float, input().split())

bhas(a, b, c)


