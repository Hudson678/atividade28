# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar

produtos = []
estoque = []

for n in range(5):
    nome_produto = str(input(f"insira o nome do produto {n+1}: "))
    num_estoque = int(input(f"quantos tem no estoque {n+1}: "))
    
    produtos.append(nome_produto)
    estoque.append(num_estoque)
    
naotem = []

for i in range(5):
    if estoque[i] == 0:
        naotem.append(produtos[i])

if naotem:
    print(f"produtos com estoque zerado: {', '.join(naotem)}")
else:
    print ("sem produtos zerador no estoque")
