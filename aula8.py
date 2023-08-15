estoque = {"Max Steel": [100, 119.99], "Barbie": [400, 139.99], "Hot Wheels":[120, 39.99]}

venda = [["Max Steel", 73], ["Barbie", 324], ["Hot Wheels", 93]]

total = 0
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto}: {quantidade} x {preco} = {custo}")
    estoque[produto][0] -= quantidade
    total += custo

print(f'Custo total: {total}')

for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço: R$ {dados[1]}")
