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

def temGanhador():
    """Verificação para saber se tem ganhador"""

    for line in range(3):
        if (
            tabuleiro[line][0] != " " and
            tabuleiro[line][0] == tabuleiro[line][1] and
            tabuleiro[line][0] == tabuleiro[line][2]
        ):
            print(f"{tabuleiro[line][0]} GANHOUUUU!!!!!!!! 🎆")
            return True

    """VERIFICAÇÃO DAS COLUNAS"""
    for coluna in range(3):
        if (
            tabuleiro[0][coluna] != " " and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f"{tabuleiro[0][coluna]} GANHOUUUU!!!!!!!! 🎆")
            return True
        
        if (
            tabuleiro[1][1] != " " and
            (
                (
                    tabuleiro[0][0] == tabuleiro[1][1] and
                    tabuleiro[0][0] == tabuleiro[2][2]
                ) or
                (
                    tabuleiro[0][2] == tabuleiro[1][1] and
                    tabuleiro[1][1] == tabuleiro[2][0]
                )
            )
        ):
            
            print(f"{tabuleiro[1][1]} GANHOUUUU!!!!!!!! 🎆")
            return True

    """SE NAO TEVE GANHADOR RETORNA FALSO"""
    return False

def temEmpate():
    for line in range(3):
        for coluna in range(3):
            if tabuleiro[line][coluna] == " ":
                return False
    print("Acabou empatado!")
    return True


while True:
    print(f"A vez de jogar é do: ({jogador}) ")
    try:
        line = int(input("Em qual linha você vai jogar? "))
        coluna = int(input("Em qual coluna você vai jogar? "))
        jogador = jogada(line, coluna)
    except (ValueError, IndexError):
        print("Digite valores numericos entre 0 e 2. ")
    
    showTabuleiro()
    if temGanhador() or temEmpate():
        break
    
