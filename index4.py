import json

def calcular_estatisticas_faturamento(dados_faturamento):
    faturamento_diario = dados_faturamento["faturamento_diario"]

    # Filtra os dias com faturamento para calcular a média
    dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]

    # Calcula as estatísticas
    menor_valor = min(dias_com_faturamento)
    maior_valor = max(dias_com_faturamento)
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    dias_acima_da_media = len([valor for valor in dias_com_faturamento if valor > media_mensal])

    return menor_valor, maior_valor, dias_acima_da_media

def main():
    # Lê os dados do arquivo JSON
    with open('faturamento.json') as json_file:
        dados_faturamento = json.load(json_file)

    # Calcula as estatísticas
    menor_valor, maior_valor, dias_acima_da_media = calcular_estatisticas_faturamento(dados_faturamento)

    # Exibe os resultados
    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Número de dias acima da média: {dias_acima_da_media}")

if __name__ == "__main__":
    main()