# MEXER AQUI
valorAtualConta = 0
AnosFuturos = 0     
taxa_anual = 0.0000  # X% do CDI, em decimal (0.0000)

# ======================================================

taxa_mensal = (1 + taxa_anual)**(1/12) - 1

montante = valorAtualConta
meses_futuros = AnosFuturos * 12
for i in range(meses_futuros):
    montante = montante * (1 + taxa_mensal)

print(f"Valor atual da conta: R$ {valorAtualConta:.2f}")
print(f"Valor daqui a {AnosFuturos} anos: R$ {montante:.2f}")
print(f"Lucro projetado: R$ {montante - valorAtualConta:.2f}")
