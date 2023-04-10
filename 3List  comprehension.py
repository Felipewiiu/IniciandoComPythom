lista_precos = [500, 1500, 2000, 100, 25]

# caso 1
novaListaPrecos = []
# para cada preço na lista de preço
for precos in lista_precos:
    novaListaPrecos.append(precos * 2)
print(novaListaPrecos)

# Caso 2
novaListaPrecos2 = [precos * 2 for precos in lista_precos]

