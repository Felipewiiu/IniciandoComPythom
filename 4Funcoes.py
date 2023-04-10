
# Uma função pode ter um parâmetro com um valor padrão
def produto (produto = "Computador"):
    print("produto: " + produto)
    print("produto: " + 'Mouse')
    print("produto: " + 'Monitor')

produto()

# Usando a recusividade nas funções

def testa_recursao(valor):
    if valor > 0:
        result = valor + testa_recursao(valor - 1)
        print(result)
    else:
        result = 0
        return result

print("\n\nResultado da recursão ")
testa_recursao(8)