def analisar_sequencia_pares(limite):
    resultado = []

    for numero in range(1, limite + 1):
        if numero % 2 == 0 and numero % 3 == 0:
            resultado.append(numero)

    return resultado

