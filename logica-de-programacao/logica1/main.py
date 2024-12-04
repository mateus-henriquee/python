# -*- coding: utf-8 -*-
import time


# Entrada de números
n1 = float(input("Escreva Um Numero Qualquer: "))
time.sleep(1)

n2 = float(input("Escreva Um Outro Numero Qualquer: "))
time.sleep(1)


# Entrada da operação
option = input("Escolha Qual Operação (Soma, Menos, Dividir ou Multiplicar): ").lower()  # Corrigido para .lower()


# Operações:
# Soma:
if option == "soma":
    resultado = n1 + n2
    print(f"Resultado da Soma: {resultado}")


# Subtração:
elif option == "menos":
    resultado = n1 - n2
    print(f"Resultado da Subtração: {resultado}")


# Divisão:
elif option == "dividir":
    if n2 != 0:  # Prevenção de divisão por zero
        resultado = n1 / n2
        print(f"Resultado da Divisão: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")

# Multiplicar:
elif option == "multiplicar":
    resultado = n1 * n2
    print(f"Resultado da Multiplicação: {resultado}")


# Confirmando O Input De Operação Do Úsuario
else:
    print("Operação inválida. Por favor, escolha entre Soma, Menos, Dividir ou Multiplicar.")