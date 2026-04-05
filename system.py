print("Bem vindo ao TrabyBank")
print("-----------------------")

while True:
    print("1. CADASTRO DE NOVO USUARIO")
    print("2. Buscar lista de clientes ativos")
    option = input("Escolha sua opção: ")


    match option:
            case "1":
                print()
                print("CADASTRO DE NOVO USUARIO")

                users = []
                name = input("Digite seu nome completo: ")
                first_name = name.split()[0]
                cpf = input(f"Muito bem {first_name},agora precisamos que você nos forneça seu CPF: ")

                user = {
                   "nome": name,
                    "cpf": cpf
                }

                users.append(user)
            case "2":
                print()
                print("Buscar lista de clientes ativos")
                print(user)
                print()
