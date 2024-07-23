def res(a_in, b_in):
    res = a_in + b_in
    numero = [int(numero) for numero in str(res)]

    for i in numero:
        if numero[i] > 1:
            numero[i] = 0
        i+=1

    final = str(''.join(map(str, numero)))

    d_final = int(final,2)
    
    return d_final

a,b = map(int, input().split())
c,d = map(int, input().split())

a_bin = bin(a)[2:]
b_bin = bin(b)[2:]
c_bin = bin(c)[2:]
d_bin = bin(d)[2:]

a_in = int(a_bin)
b_in = int(b_bin)
c_in = int(c_bin)
d_in = int(d_bin)


res1 = res(a_in, b_in)
res2 = res(c_in, d_in)

print(res1)
print(res2)                     