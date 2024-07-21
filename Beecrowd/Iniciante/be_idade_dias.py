N = int(input())
ano = mes = dia = 0

while N != 0:
    if (N >= 365):
        N -= 365
        ano += 1
    elif (N < 365 and N >= 30):
        N -= 30
        mes += 1
    else:
        dia = N
        N = 0

print(f'{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)')