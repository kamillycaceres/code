# Definindo os valores de faturamento mensal por estado
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculando o valor total mensal da distribuidora
total_mensal = sum(faturamento_por_estado.values())

# Calculando o percentual de representação de cada estado
percentuais_por_estado = {}
for estado, faturamento in faturamento_por_estado.items():
    percentual = (faturamento / total_mensal) * 100
    percentuais_por_estado[estado] = percentual

# Exibindo os resultados
print("Percentual de representação de cada estado no faturamento mensal da distribuidora:")
for estado, percentual in percentuais_por_estado.items():
    print(f"{estado}: {percentual:.2f}%")
