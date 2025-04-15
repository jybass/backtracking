def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|"," | ".join(str(espaco) for espaco in linha),"|")

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    melhor_profundidade = float('inf')
    melhor_linha = linha_atual
    melhor_coluna = coluna_atual

    direcoes = {
        'direita': (0, 1),
        'esquerda': (0, -1),
        'cima': (-1, 0),
        'baixo': (1, 0)
    }

    for direcao, (dire_linha, dire_coluna) in direcoes.items():
        nova_linha = linha_atual + dire_linha
        nova_coluna = coluna_atual + dire_coluna

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            if chegou_destino(nova_linha, nova_coluna):
                return (nova_linha, nova_coluna, profundidade)
            else:
                tabuleiro[nova_linha][nova_coluna] = '*'
                res = proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1)
                tabuleiro[nova_linha][nova_coluna] = ' '

            if res[2] < melhor_profundidade:
                melhor_profundidade = res[2]
                melhor_linha = nova_linha
                melhor_coluna = nova_coluna

    return (melhor_linha,melhor_coluna,melhor_profundidade)

def movimento_valido(tabuleiro,linha,coluna):
    numero_linha = len(tabuleiro)
    numero_coluna = len(tabuleiro[0])
    return 0 <= linha < numero_linha and 0 <= coluna < numero_coluna and tabuleiro[linha][coluna] == ' '

def chegou_destino(linha_atual, coluna_atual):
    if linha_atual == 0 and coluna_atual == 3:
        return True

def main():
    tabuleiro = [
        [' ', ' ', ' ', ' '],
        [' ', 'X', ' ', ' '],
        [' ', ' ', 'X', ' '],
        [' ', ' ', 'X', ' ']
    ]
    posicao_linha = 3
    posicao_coluna = 0
    tabuleiro[posicao_linha][posicao_coluna] = '*'

    print("Tabuleiro inicial:")
    mostrar_tabuleiro(tabuleiro)

    while not chegou_destino(posicao_linha, posicao_coluna):
        movimento = proximo_movimento(tabuleiro, posicao_linha, posicao_coluna, profundidade=1)

        if movimento[2] == float('inf'):
            print("Não foi possível encontrar um caminho para o destino!")
            break

        posicao_linha, posicao_coluna = movimento[0], movimento[1]
        tabuleiro[posicao_linha][posicao_coluna] = '*'

        print(f"Movimento para ({posicao_linha}, {posicao_coluna}) com profundidade {movimento[2]}")
        mostrar_tabuleiro(tabuleiro)

        if chegou_destino(posicao_linha, posicao_coluna):
            print("Destino alcançado!")
main()
