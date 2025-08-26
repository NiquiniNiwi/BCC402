from collections import defaultdict, deque
import random

def eulerian_cycle(graph, start, edges_count):
    """Hierholzer’s algorithm: retorna um ciclo Euleriano"""
    stack = [start] # pilha para simular DFS
    path = [] # caminho final
    used = defaultdict(int) # marca arestas já usadas

    while stack: 
        u = stack[-1] #Pega o vértice do topo da pilha (u).
        while graph[u] and used[(u, graph[u][-1])] > 0:
            graph[u].pop() #Remove arestas já usadas (se used[(u,v)] > 0).
        if graph[u]:
            v = graph[u].pop() # pega um vizinho
            used[(u, v)] += 1 # marca a aresta (u,v) como usada
            used[(v, u)] += 1 # como o grafo é não-direcionado, marca também (v,u)
            stack.append(v) # continua explorando
        else:
            path.append(stack.pop()) # se não tem mais vizinhos, fecha o caminho
    path.reverse() # O caminho é construído de trás para frente → por isso faz reverse().
    return path

def resolver(arquivo):
    with open(arquivo, "r") as f:
        dados = f.read().strip().splitlines()

    T = int(dados[0])
    idx = 1
    resultados = []

    for caso in range(1, T+1):
        N = int(dados[idx]); idx += 1 #número de contas (arestas).
        graph = defaultdict(list) #lista de adjacência.
        grau = defaultdict(int) #grau de cada vértice.
        beads = [] #lista dos pares lidos.

        for _ in range(N):
            a, b = map(int, dados[idx].split())
            idx += 1
            beads.append((a, b)) #Cada linha é um par (a, b) → aresta do grafo.
            graph[a].append(b) #Como o grafo é não-direcionado, adiciona a → b e b → a.
            graph[b].append(a) 
            grau[a] += 1 #Atualiza os graus dos vértices.
            grau[b] += 1

        # Verificar se todos os vértices têm grau par
        possivel = all(g % 2 == 0 for g in grau.values())

        # Verificar se o grafo é conexo
        if possivel:
            start = beads[0][0]
            visitados = set()
            fila = deque([start])
            while fila:
                u = fila.popleft()
                if u in visitados: 
                    continue
                visitados.add(u)
                for v in graph[u]:
                    fila.append(v)
            usados = {x for x in grau if grau[x] > 0} #Faz BFS a partir de um vértice com grau > 0.
            if visitados != usados: #Se nem todos os vértices usados foram visitados, não é conexo → impossível.
                possivel = False

        resultados.append(f"Case #{caso}")
        if not possivel:  #Se não for possível formar ciclo Euleriano → escreve "some beads may be lost".
            resultados.append("some beads may be lost")
        else:
            cycle = eulerian_cycle(defaultdict(list, {k:list(v) for k,v in graph.items()}),
                                   beads[0][0], N)
            # O ciclo é uma lista de vértices, precisamos transformá-lo em arestas
            for i in range(1, len(cycle)):
                resultados.append(f"{cycle[i-1]} {cycle[i]}")
        resultados.append("")  # linha em branco entre casos

    return "\n".join(resultados).strip()


# Exemplo de uso
if __name__ == "__main__":
    n = random.randint(1,6)
    print(f"Entrada {n}")
    print(resolver(f"C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-9.2\\entrada{n}.txt"))
