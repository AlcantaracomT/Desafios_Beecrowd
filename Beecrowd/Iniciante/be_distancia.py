import math

x,x1 = map(float, input().split())
y,y1 = map(float, input().split())

x-=y
y1-=x1

distancia = math.sqrt((pow(x,2)) + (pow(y1,2)))

print(f'{distancia:.4f}')