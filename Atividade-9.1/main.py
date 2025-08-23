from collections import deque

def bfs(inicial, alvo, proibidos):
    if inicial in proibidos:
        return -1
    if inicial == alvo:
        return 0

    fila = deque([(inicial, 0)])
    visitados = {inicial}

    while fila:
        atual, dist = fila.popleft()
        for viz in vizinhos(atual): #Para cada vizinho (nova configuração ao girar 1 dígito da roda)
            if viz not in visitados and viz not in proibidos: #Se ainda não foi visitado e não está em proibidos → seguimos.
                if viz == alvo: #Se for exatamente o alvo → retornamos dist + 1 (achamos a resposta mínima!).
                    return dist + 1
                visitados.add(viz) #Marcamos como visitado.
                fila.append((viz, dist + 1)) #Colocamos na fila com distância dist + 1.
    return -1 #Se exploramos todo o grafo e não chegamos ao alvo → impossível.

def vizinhos(config):
    for i in range(4): #Gera todas as configurações vizinhas. Para cada uma das 4 rodas (i de 0 a 3)
        for delta in (-1, 1): #Tenta girar +1 ou -1 (delta).
            novo = list(config)
            novo[i] = (novo[i] + delta) % 10 #Usa % 10 para "dar a volta" (ex.: 9 + 1 = 0, 0 - 1 = 9).
            yield tuple(novo) #significa que essa função é um gerador → podemos iterar sobre os vizinhos facilmente.

def resolver(arquivo):
    with open(arquivo, "r") as f:
        dados = f.read().strip().splitlines()

    t = int(dados[0]) #qtd de problemas
    idx = 1
    resultados = []
    
    for _ in range(t):
        inicial = tuple(map(int, dados[idx].split())); idx += 1
        alvo = tuple(map(int, dados[idx].split())); idx += 1
        n = int(dados[idx]); idx += 1
        proibidos = set()
        for _ in range(n):
            proibidos.add(tuple(map(int, dados[idx].split())))
            idx += 1
        if idx < len(dados) and dados[idx] == "": #ENTER
            idx += 1
        resultados.append(bfs(inicial, alvo, proibidos)) #chamada da solução do problema

    return resultados


# Exemplo de uso:
resultados = resolver("C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-9.1\\entrada1.txt")
for r in resultados:
    print(r)
