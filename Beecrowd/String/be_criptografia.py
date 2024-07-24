import sys

def asc(a):
    for i in range(len(a)):
        a[i] = ord(a[i])
    return a

def cesar(a,n):
    if n:
        for i in range(len(a)):
            if 97 <= a[i] <= 122 or 65 <= a[i] <= 90:
                a[i] = chr(a[i] +3)
            else:
                a[i] = chr(a[i])
        a.reverse()
    else:
        for i in range(len(a)):
            if(32 <= a[i] <= 126):
                a[i] = chr(a[i] -1 )

def main():
    
    o = int(input())
    a = []
    
    for i in range(o):
        a.append(input())

    tama_str = len(a)

    for i in range(tama_str): 
        n = True
        l = list(a[i])
        asc(l)
        cesar(l,n)

        tam = len(l) 
        b = l[:(tam//2)]

        l = l[(tam//2):tam]

        n = False
        asc(l)
        cesar(l,n)


        l = ''.join(l)
        b = ''.join(b)

        print(b+l)
        i -= 1

if __name__ == "__main__":
    main()