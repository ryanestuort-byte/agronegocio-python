import json

culturas = []


def cadastrar_cultura():
    nome = input("Nome da cultura: ")
    area = float(input("Área em m²: "))
    produto = input("Produto utilizado: ")
    dosagem = float(input("Dosagem por m²: "))

    insumo = area * dosagem

    cultura = {
        "nome": nome,
        "area": area,
        "produto": produto,
        "insumo": insumo
    }

    culturas.append(cultura)
    print("Cultura cadastrada com sucesso!")


def listar_culturas():
    for c in culturas:
        print(f"Nome: {c['nome']}")
        print(f"Área: {c['area']} m²")
        print(f"Produto: {c['produto']}")
        print(f"Insumo necessário: {c['insumo']}")
        print("-" * 20)


def salvar_dados():
    with open("dados.json", "w") as f:
        json.dump(culturas, f)
    print("Dados salvos!")


def carregar_dados():
    global culturas
    try:
        with open("dados.json", "r") as f:
            culturas = json.load(f)
    except:
        culturas = []


def menu():
    carregar_dados()

    while True:
        print("\n1 - Cadastrar")
        print("2 - Listar")
        print("3 - Salvar")
        print("4 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_cultura()
        elif op == "2":
            listar_culturas()
        elif op == "3":
            salvar_dados()
        elif op == "4":
            break
        else:
            print("Opção inválida!")


menu()