import sys

# Direções: mover o espaço (0) trocando com o vizinho
DIRS = {
    'R': (0,  1),
    'L': (0, -1),  # 0 vai para a esquerda (troca com peça à esquerda)    
    'U': (-1, 0),
    'D': ( 1, 0),
}
OPPOSITE = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}

GOAL = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
POS_GOAL = {v: (i//4, i%4) for i, v in enumerate(GOAL)}  # posição alvo (linha,coluna) de cada valor

def inversions_and_blank_row_from_bottom(board):
    arr = [x for x in board if x != 0] #Cria uma lista arr com todos os números do puzzle, menos o 0
    inv = 0
    for i in range(len(arr)): #Calcula o número de inversões
        ai = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < ai:
                inv += 1
    idx0 = board.index(0) #posição (índice) do espaço vazio no tabuleiro.
    r0 = idx0 // 4 #Converte o índice em linha (0 a 3)
    row_from_bottom = 4 - r0  # 1 (fundo) .. 4 (topo)
    return inv, row_from_bottom #Retorna o número de inversões e a posição do zero (em relação ao fundo)

def is_solvable(board):
    '''
    Determina se o puzzle é solúvel.
    Fórmula: em um tabuleiro 4×4, inversões + linha_do_zero precisa ser ímpar.
    Retorna True se for solúvel, False caso contrário.
    '''
    inv, rb = inversions_and_blank_row_from_bottom(board)
    return ((inv + rb) & 1) == 1

def backtrack(board, zr, zc, depth, max_depth, path, last_move):
    '''
    Define a função recursiva para resolver o puzzle com backtracking.
    board = estado atual do tabuleiro.
    zr, zc = posição do espaço vazio (linha e coluna).
    depth = profundidade atual da recursão (quantos movimentos já fez).
    max_depth = limite de movimentos (50).
    path = lista com os movimentos feitos até agora.
    last_move = último movimento realizado (para evitar desfazer imediatamente).
    '''
    if board == GOAL: #Caso base 1: se o tabuleiro já é igual ao objetivo, encontramos a solução
        return True
    if depth >= max_depth: #Caso base 2: se já fez 50 movimentos, para (não procura mais fundo).
        return False
    for mv, (dr, dc) in DIRS.items():
        if last_move and mv == OPPOSITE[last_move]: #Evita voltar atrás imediatamente. Exemplo: se o último movimento foi L, não tenta R agora.
            continue  # não desfazer o último passo
        nr, nc = zr + dr, zc + dc
        if 0 <= nr < 4 and 0 <= nc < 4: #Só continua se o novo espaço vazio ficar dentro do tabuleiro (4×4).
            i0 = zr*4 + zc #Converte as coordenadas (linha, coluna) em índices na lista board. Exemplo: (linha=2, coluna=3) → 2*4 + 3 = 11.
            i1 = nr*4 + nc
            board[i0], board[i1] = board[i1], board[i0]  # Troca o espaço vazio (0) com a peça vizinha → simula o movimento
            path.append(mv)
            if backtrack(board, nr, nc, depth+1, max_depth, path, mv): #chamada recursiva
                return True
            path.pop() #Se não encontrou solução, remove o último movimento (desfaz caminho). 
            board[i0], board[i1] = board[i1], board[i0]  # Desfaz a troca no tabuleiro (volta ao estado anterior).
    return False #Se tentou todos os movimentos possíveis e nenhum levou à solução, retorna False.

def solve(board):
    if not is_solvable(board):
        return "This puzzle is not solvable."
    zr, zc = divmod(board.index(0), 4) #Encontra a posição do espaço vazio.
    path = [] #Cria lista vazia para guardar a sequência de movimentos.
    if backtrack(board, zr, zc, 0, 50, path, None):
        return "".join(path)
    else:
        return "This puzzle is not solvable."

def main():
    with open('C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-8\\entrada2.txt', "r") as f:
        linhas = [linha.strip() for linha in f.readlines() if linha.strip()]

    qtd_tabuleiros = int(linhas[0])   # primeira linha
    tabuleiros = []

    for i in range(qtd_tabuleiros):
        inicio = 1 + i * 4
        fim = inicio + 4
        # junta as 4 linhas do tabuleiro em uma só lista
        tabuleiro = []
        for j in range(inicio, fim):
            tabuleiro.extend(map(int, linhas[j].split()))
        tabuleiros.append(tabuleiro)
    out = []
    for tabuleiro in tabuleiros:
        out.append(solve(tabuleiro))
    print("\n".join(out))

if __name__ == "__main__":
    main()