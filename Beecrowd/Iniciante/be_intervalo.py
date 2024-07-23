def intervalo(n):
    if 0.0 <= n <= 25.0:
        return print("Intevalo [0,25]")
    elif  25.0 < n <= 50.0:
        return print("Intevalo (25,50]")
    elif 50.0 < n <= 75.0:
        return print("Intevalo (50,75]")
    elif 75.0 < n <= 100.0:
        return print("Intevalo (75,100]")
    else:
        print('Fora de intervalo')

a = float(input())

intervalo(a)