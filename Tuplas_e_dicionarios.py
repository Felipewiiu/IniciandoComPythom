# Funcionamento da tupla

professores = ("Fernando", "Beatriz", "Carlos")

# professores[0] = "nana" --> isso não funciona

print(professores)










# criação do dicionário

aluno = {
    "nome": "Felipe",
    "Sobre nome": "Oliveira"
}

for x,y in aluno.items():
    print(x,y, "\n\n")

# Outro exemplo de dicionário

automovel = {
    'marca': 'Ford',
    'modelo': 'Mustang',
    'ano': 2019
}

# Aqui se faz um for em um dicionário


print("*" * 60)

for chave, valor in automovel.items():
    print(chave, valor)

# Adição de elemetos em um dicionário

automovel_clube = {
    'marca': 'Ford',
    'modelo': 'Mustang',
    'ano': 2019
}

automovel_clube["cor"] = "Vermelho"
print(automovel_clube)

# Deletando itens de um dicionário

del automovel_clube ["cor"]

print(f"Cor deletada {automovel_clube}")


    