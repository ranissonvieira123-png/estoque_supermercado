estoque = []

while True:

    menu = int(input( '''
    ----- Gerenciamento de estoque -----
    [1] Cadastrar Produto
    [2] Atualizar Produto
    [3] Remover Produto
    [4] Mostrar Estoque
    [5] Realizar Venda
    [6] Sair"

    Escolha uma opção: '''))

    if menu == 1:  # Cadastrar Produto
        produto = {}
        produto['nome'] = input("Digite o nome do produto: ")
        produto['quantidade'] = int(input("Digite a quantidade em estoque: "))
        produto['preco'] = float(input("Digite o preço unitário do produto: "))
        estoque.append(produto)
        print('Produto cadastrado com sucesso!')

    elif menu == 2: # Atualizar Produto
        nome = input("Digite o nome do produto que deseja atualizar: ")
        for item in estoque:
            if item['nome'] == nome:
                item['quantidade'] = int(input("Digite a nova quantidade em estoque: "))
                item['preco'] = float(input("Digite o novo preço do produto: "))
                print('Produto atualizado com sucesso!')
                break
        else:
            print('Produto não encontrado!')

    elif menu == 3: # Remover Produto
        nome = input('Digite o nome do produto que deseja remover: ')
        for produto in estoque:
            if produto['nome'] == nome:
                estoque.remove(produto)
                print('Produto removido com sucesso!')
                break
        else:
            print('Produto não encontrado!')

    elif menu == 4: #  Estoque
        print('Estoque de Produtos:')
        for produto in estoque:
            print('Nome:', produto['nome'])
            print('Quantidade:', produto['quantidade'])
            print('Preço:', produto['preco'])
            print()

    elif menu == 5: #  Venda
        nome = input('Digite o nome do produto que foi vendido: ')
        quantidade = int(input('Quantidade vendida: '))
        for produto in estoque:
            if produto['nome'] == nome:
                if produto['quantidade'] >= quantidade:
                    produto['quantidade'] -= quantidade
                    total_venda = quantidade * produto['preco']
                    print(f'\n{quantidade} unidades de {nome} vendidas com sucesso!\n')
                    print(f'\nTotal de vendas: R${round(total_venda, 2)}\n')
                else:
                    print('Quantidade insuficiente em estoque!')
                break
        else:
            print('Produto não encontrado!')

    elif menu == 6:# Sair
        print('Encerrando o programa...')
        break

    else:
        print('Por favor, escolha uma opção válida.')
