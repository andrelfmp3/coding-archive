# MEXER AQUI 
anosQueGuardouDinheiro = 0
anosPassaram = 0
aporte_mensal = 0
taxa_anual = 0.0000  # X% do CDI, em decilam (0.0000)

# ======================================================

meses_aporte = anosQueGuardouDinheiro * 12
meses_total = anosPassaram * 12
taxa_mensal = (1 + taxa_anual)**(1/12) - 1
dinheiroGuardado = anosQueGuardouDinheiro * 12 * aporte_mensal

montante = 0
for i in range(meses_aporte):
    montante = montante * (1 + taxa_mensal) + aporte_mensal

meses_sem_aporte = meses_total - meses_aporte
for i in range(meses_sem_aporte):
    montante = montante * (1 + taxa_mensal)
    
print(f"Valor final após {anosPassaram} anos: R$ {montante:.2f}")
print(f"Você guardou: R$ {dinheiroGuardado}")
print(f"Lucro: R$ {montante - dinheiroGuardado:.2f}")
