nome = input()
salario = float(input())
vendas = float(input())

bonus = (vendas * 15/100)

print(f'TOTAL = R$ {(salario + bonus):.2f}')