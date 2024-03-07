def verifica_fibonacci(numero):
  a, b = 0, 1

  while b < numero:
      a, b = b, a + b

  if b == numero:
      return True
  else:
      return False

# Exemplo: você pode alterar o valor de 'numero' conforme necessário
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if verifica_fibonacci(numero):
  print(f"{numero} pertence à sequência de Fibonacci.")
else:
  print(f"{numero} não pertence à sequência de Fibonacci.")