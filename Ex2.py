def filtrar_acima_da_media(lista_numeros):
    if not lista_numeros:
        return []

    media_aritmetica = sum(lista_numeros) / len(lista_numeros)
    resultado = [numero for numero in lista_numeros if numero > media_aritmetica]
    return resultado

print(filtrar_acima_da_media([1, 2, 3, 4, 5]))