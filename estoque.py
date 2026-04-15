import json

def salvarEstoque():
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo)

def carregarEstoque():
    try:
        with open("estoque.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {
            "banana": 10,
            "maçã": 5,
            "laranja": 8,
            "cenoura": 4
        }
    
estoque = carregarEstoque()

for nome, quantidade in estoque.items():
    print(f"{nome}: {quantidade}")


def adicionarProduto():
    novoProduto = input("Adicione um novo porduto: ")
    quantidadeNovoProduto = int(input("Adicione a quantidade: "))

    estoque[novoProduto] = quantidadeNovoProduto

    for nome, quantidade in estoque.items():
        print(f"{nome}: {quantidade}")

    salvarEstoque()



def removerProduto():
    nomeProduto = input("Qual produto voce deseja remover? ")

    estoque.pop(nomeProduto)
    for nome, quantidade in estoque.items():
        print(f"{nome}: {quantidade}")

    salvarEstoque()


def atualizarQuantidade():
    produto = input("Qual o produto que deseja para aumentar a quantidade? ")
    if produto in estoque:
        quantidadeProduto = int(input("Qual a quantidade que deseja adicionar? "))
    else:
        return print("Produto não encontrado.")

    estoque[produto] = quantidadeProduto + estoque[produto]
    
    for nome, quantidade in estoque.items():
        print(f"{nome}: {quantidade}")
    
    salvarEstoque()


def exibirMenu():
    print("1 - Ver estoque\n2 - Adicionar produto\n3 - Remover produto\n4 - Atualizar quantidade\n5 - Sair")


  

while True:
    exibirMenu()
    opcao = int(input("Digite o numero desejado: "))
    
    if opcao == 1:
         for nome, quantidade in estoque.items():
            if quantidade <= 5:
               print(f"{nome}: {quantidade} ⚠️  Estoque baixo!")
            else:
             print(f"{nome}: {quantidade}")
     
           

    elif opcao == 2:
        adicionarProduto()
    elif opcao == 3:
        removerProduto()
    elif opcao == 4:
        atualizarQuantidade()
    elif opcao == 5:
        print("Saindo...")
        break






exibirMenu()