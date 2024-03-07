# Função para inverter uma string sem usar funções prontas
def inverter_string(input_string):
    # Converte a string para uma lista de caracteres
    lista_caracteres = list(input_string)

    # Obtém o comprimento da string
    comprimento = len(lista_caracteres)

    # Inverte os caracteres usando um loop
    for i in range(comprimento // 2):
        # Troca os caracteres i e comprimento - 1 - i
        lista_caracteres[i], lista_caracteres[comprimento - 1 - i] = lista_caracteres[comprimento - 1 - i], lista_caracteres[i]

    # Converte a lista de caracteres de volta para uma string
    string_invertida = ''.join(lista_caracteres)

    return string_invertida

# Exemplo: você pode alterar o valor da variável 'entrada' conforme necessário
entrada = input("Digite uma string para inverter: ")
resultado = inverter_string(entrada)

# Exibe o resultado
print("String invertida:", resultado)