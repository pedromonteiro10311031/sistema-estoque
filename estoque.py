estoque = {
    "banana": 10,
    "maçã": 5,
    "laranja": 8,
    "cenoura": 4,
    
}

for nome, quantidade in estoque.items():
    print(f"{nome}: {quantidade}")


def adicionarProduto():
    novoProduto = input("Adicione um novo porduto: ")
    quantidadeNovoProduto = int(input("Adicione a quantidade: "))

    estoque[novoProduto] = quantidadeNovoProduto

    for nome, quantidade in estoque.items():
        print(f"{nome}: {quantidade}")



def removerProduto():
    nomeProduto = input("Qual produto voce deseja remover? ")

    estoque.pop(nomeProduto)
    for nome, quantidade in estoque.items():
        print(f"{nome}: {quantidade}")


def atualizarQuantidade():
    produto = input("Qual o produto que deseja para aumentar a quantidade? ")
    quantidadeProduto = int(input("Qual a quantidade que deseja adicionar? "))

    estoque[produto] = quantidadeProduto + estoque[produto]
    
    for nome, quantidade in estoque.items():
        print(f"{nome}: {quantidade}")




atualizarQuantidade()
adicionarProduto()
removerProduto()
