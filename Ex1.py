quantidade_produtos = int(input("Quantidade de produtos: "))

nome_maior_quantidade = ""
maior_quantidade = 0
nome_maior_valor = ""
maior_valor = 0

for i in range(quantidade_produtos):
    produto = input("Produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    valor_estoque = preco * quantidade

    if i == 0 or quantidade > maior_quantidade:
        maior_quantidade = quantidade
        nome_maior_quantidade = produto

    if i == 0 or valor_estoque > maior_valor:
        maior_valor = valor_estoque
        nome_maior_valor = produto

print(f"Produto com maior quantidade: {nome_maior_quantidade}")
print(f"Produto com maior valor em estoque: {nome_maior_valor}")