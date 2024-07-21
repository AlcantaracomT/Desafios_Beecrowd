peca1, pec1, pe1 = input().split()
peca2, pec2, pe2 = input().split()

peca1 = int(peca1)
pec1 = int(pec1)
pe1 = float(pe1)

peca2 = int(peca2)
pec2 = int(pec2)
pe2 = float(pe2)

print(f'VALOR A PAGAR {(pec1*pe1)+(pec2*pe2):.2f}')