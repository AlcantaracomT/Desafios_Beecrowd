N = 140153

hora = N//3600

min = (N%3600)//60

seg = N%60



print(f'{hora:.0f}:{min:.0f}:{seg:.0f}')