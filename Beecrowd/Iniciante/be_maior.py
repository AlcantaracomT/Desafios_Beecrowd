a, b, c = map(int, input().split())

ab = ((a+b + abs(a-b)))/2
abc = ab+c

maior = int((abc + abs(ab - c))/2)

print(f'{maior} eh o maior')