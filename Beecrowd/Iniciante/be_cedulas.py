N = int(input())
cem=cin=vin=dez=cinc=dois=um=0

while N != 0:
    if(N >= 100):
        cem += 1
        N -= 100
    elif(N >= 50):
        cin += 1
        N -= 50
    elif(N >= 20):
        vin += 1
        N -= 20
    elif(N >= 10):
        dez+= 1 
        N -= 10
    elif(N >= 5):
        cinc += 1
        N -= 5
    elif(N >= 2):
        dois += 1
        N -= 2
    elif(N >= 1):
        um = 1
        N -= 1

print(f'{cem} nota(s) de R$ 100,00\n{cin} nota(s) de R$ 50,00\n{vin} nota(s) de R$ 20,00\n{dez} nota(s) de R$ 10,00\n{cinc} nota(s) de R$ 5,00\n{dois} nota(s) de R$ 2,00\n{um} nota(s) de R$ 1,00\n')