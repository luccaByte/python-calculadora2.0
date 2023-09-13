def soma(n1, n2):
  return n1 + n2

def subtracao(n1, n2):
  return n1 - n2
  
def multi(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

while True:
  print("Escolha um número para o cálculo:")
  print("1: Soma")
  print("2: Subtração")
  print("3: Multiplicação")
  print("4: Divisão")
  print("5: SAIR")

  entrada = input("Digite o número escolhido: ")

  if entrada == "5":
    print("Você escolheu SAIR, volte sempre!")
    break

  elif entrada == "1":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    res = soma(n1, n2)
    print("Resultado da soma: ", res)

  elif entrada == "2":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    res = subtracao(n1, n2)
    print("Resultado da subtração: ", res)

  elif entrada == "3":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    res = multi(n1, n2)
    print("Resultado da multiplicação: ", res)

  elif entrada == "4":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    res = div(n1, n2)
    print("Resultado da divisão: ", res)

  else:
    print("[ERROR 404] - Tente novamente!")
