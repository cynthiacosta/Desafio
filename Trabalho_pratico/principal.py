import csv

# Estruturas de dados para usuários e produtos
usuarios = []
produtos = []

# Funções para gerenciar usuários
def carregar_usuarios():
    try:
        with open('usuarios.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                usuarios.append(row)
    except FileNotFoundError:
        pass  # Arquivo não encontrado, continuar sem carregar usuários

def salvar_usuarios():
    with open('usuarios.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "nome", "senha", "tipo"])
        writer.writeheader()
        writer.writerows(usuarios)

def criar_usuario(id, nome, senha, tipo):
    usuarios.append({"id": id, "nome": nome, "senha": senha, "tipo": tipo})
    salvar_usuarios()

def listar_usuarios():
    for usuario in usuarios:
        print(usuario)

def atualizar_usuario(id, nome, senha, tipo):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = nome
            usuario["senha"] = senha
            usuario["tipo"] = tipo
    salvar_usuarios()

def remover_usuario(id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario["id"] != id]
    salvar_usuarios()

# Funções para gerenciar produtos
def carregar_produtos():
    try:
        with open('produtos.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['preco'] = float(row['preco'])
                row['quantidade'] = int(row['quantidade'])
                produtos.append(row)
    except FileNotFoundError:
        pass  # Arquivo não encontrado, continuar sem carregar produtos

def salvar_produtos():
    with open('produtos.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "nome", "preco", "quantidade"])
        writer.writeheader()
        writer.writerows(produtos)

def criar_produto(id, nome, preco, quantidade):
    produtos.append({"id": id, "nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos()

def listar_produtos():
    for produto in produtos:
        print(produto)

def atualizar_produto(id, nome, preco, quantidade):
    for produto in produtos:
        if produto["id"] == id:
            produto["nome"] = nome
            produto["preco"] = preco
            produto["quantidade"] = quantidade
    salvar_produtos()

def remover_produto(id):
    global produtos
    produtos = [produto for produto in produtos if produto["id"] != id]
    salvar_produtos()

def buscar_produto(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print(produto)

def ordenar_produtos_por_nome():
    produtos_ordenados = sorted(produtos, key=lambda x: x["nome"])
    for produto in produtos_ordenados:
        print(produto)

def ordenar_produtos_por_preco():
    produtos_ordenados = sorted(produtos, key=lambda x: x["preco"])
    for produto in produtos_ordenados:
        print(produto)

# Funções auxiliares para login e controle de acesso
def login(nome, senha):
    for usuario in usuarios:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            return usuario
    return None

def menu_gerente():
    print("\nMenu Gerente")
    print("1. Listar Usuários")
    print("2. Criar Usuário")
    print("3. Atualizar Usuário")
    print("4. Remover Usuário")
    print("5. Listar Produtos")
    print("6. Criar Produto")
    print("7. Atualizar Produto")
    print("8. Remover Produto")
    print("9. Buscar Produto por Nome")
    print("10. Ordenar Produtos por Nome")
    print("11. Ordenar Produtos por Preço")
    print("0. Sair")

def menu_funcionario():
    print("\nMenu Funcionário")
    print("1. Listar Produtos")
    print("2. Atualizar Produto")
    print("3. Buscar Produto por Nome")
    print("4. Ordenar Produtos por Nome")
    print("5. Ordenar Produtos por Preço")
    print("0. Sair")

def menu_cliente():
    print("\nMenu Cliente")
    print("1. Listar Produtos")
    print("2. Buscar Produto por Nome")
    print("0. Sair")

# Carregar dados iniciais
carregar_usuarios()
carregar_produtos()

# Interface de login
print("Bem-vindo ao sistema de gerenciamento da Book Haven")
nome = input("Nome de usuário: ")
senha = input("Senha: ")

usuario_logado = login(nome, senha)
if usuario_logado:
    tipo_usuario = usuario_logado["tipo"]
    while True:
        if tipo_usuario == "gerente":
            menu_gerente()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                listar_usuarios()
            elif opcao == "2":
                id = input("ID do novo usuário: ")
                nome = input("Nome do novo usuário: ")
                senha = input("Senha do novo usuário: ")
                tipo = input("Tipo do novo usuário (gerente, funcionario, cliente): ")
                criar_usuario(id, nome, senha, tipo)
            elif opcao == "3":
                id = input("ID do usuário a ser atualizado: ")
                nome = input("Novo nome do usuário: ")
                senha = input("Nova senha do usuário: ")
                tipo = input("Novo tipo do usuário: ")
                atualizar_usuario(id, nome, senha, tipo)
            elif opcao == "4":
                id = input("ID do usuário a ser removido: ")
                remover_usuario(id)
            elif opcao == "5":
                listar_produtos()
            elif opcao == "6":
                id = input("ID do novo produto: ")
                nome = input("Nome do novo produto: ")
                preco = float(input("Preço do novo produto: "))
                quantidade = int(input("Quantidade do novo produto: "))
                criar_produto(id, nome, preco, quantidade)
            elif opcao == "7":
                id = input("ID do produto a ser atualizado: ")
                nome = input("Novo nome do produto: ")
                preco = float(input("Novo preço do produto: "))
                quantidade = int(input("Nova quantidade do produto: "))
                atualizar_produto(id, nome, preco, quantidade)
            elif opcao == "8":
                id = input("ID do produto a ser removido: ")
                remover_produto(id)
            elif opcao == "9":
                nome = input("Nome do produto a buscar: ")
                buscar_produto(nome)
            elif opcao == "10":
                ordenar_produtos_por_nome()
            elif opcao == "11":
                ordenar_produtos_por_preco()
            elif opcao == "0":
                break
        elif tipo_usuario == "funcionario":
            menu_funcionario()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                listar_produtos()
            elif opcao == "2":
                id = input("ID do produto a ser atualizado: ")
                nome = input("Novo nome do produto: ")
                preco = float(input("Novo preço do produto: "))
                quantidade = int(input("Nova quantidade do produto: "))
                atualizar_produto(id, nome, preco, quantidade)
            elif opcao == "3":
                nome = input("Nome do produto a buscar: ")
                buscar_produto(nome)
            elif opcao == "4":
                ordenar_produtos_por_nome()
            elif opcao == "5":
                ordenar_produtos_por_preco()
            elif opcao == "0":
                break
        elif tipo_usuario == "cliente":
            menu_cliente()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                listar_produtos()
            elif opcao == "2":
                nome = input("Nome do produto a buscar: ")
                buscar_produto(nome)
            elif opcao == "0":
                break
else:
    print("Usuário ou senha incorretos")