perguntas = [
    ["Seu animal gosta de bananas", "macaco"],
    ["Seu animal é laranja e tem listras?", "tigre"],
    ["Seu animal é grande, peludo e branco?", "urso polar"]
]


name = input("Seja Bem vindo ao nosso jogo de advinhação! Qual seu nome? ")
print()
print(f"Muito bem {name} , Pense em um animal... ")

while True:
    acertou = False
    for pergunta in perguntas:
        resposta = input(f"{pergunta[0]} ? (s/n):  ")
        if resposta.lower() == "s":
            print(f"Você estava pensando em um {pergunta[1]}.")
            acertou = True
            break

    if not acertou:
        print
        print("Poxa, você me venceu, não cosnegui advinhar :/")
        new_animal = input("Qual era o nome do seu animal? ")
        new_description = input(f"{name} descreva uma dica do seu animal para mim, para eu poder aprender e lembrar dele na proxima vez ;) ")
        perguntas.append([new_description, new_animal])

    print()
    resposta = input("Quer jogar novamente? (s/n) ")
    if resposta.lower() != "s":
        print("OK! Foi bom jogar com você!" )
        break