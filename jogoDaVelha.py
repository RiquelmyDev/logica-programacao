tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

jogador = "X"

def showTabuleiro():
    for line in tabuleiro:

        print("|".join(line))
        print("-" * 5)
        #print(f"{line[0]}|{line[1]}|{line[2]}")
        #print("-----")

def jogada(line, coluna):
    if (
        not 0 <= line <= 2 or 
        not 0 <= coluna <= 2 or 
        tabuleiro[line][coluna] != " "
    ):
        print("Jogada invalida!")
        return jogador
 
    tabuleiro[line][coluna] = jogador
    return "O" if jogador == "X" else "X"

    #if jogador == "X":
    #    return "O"
    #else:
    #    return "X"
    
while True:
    print(f"A vez de jogar é do: ({jogador}) ")
    try:
        line = int(input("Em qual linha você vai jogar? "))
        coluna = int(input("Em qual coluna você vai jogar? "))
        jogador = jogada(line, coluna)
    except (ValueError, IndexError):
        print("Digite valores numericos entre 0 e 2. ")
    
    showTabuleiro()

