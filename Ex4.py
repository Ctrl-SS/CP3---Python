def calc_tempo_meta(capital_inicial, taxa_juros, meta):
    valor = capital_inicial
    meses = 0

    while valor < meta:
        valor = valor * (1 + taxa_juros / 100)
        meses = meses + 1

    return meses