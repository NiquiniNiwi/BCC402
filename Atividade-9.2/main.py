from collections import defaultdict, deque

def eulerian_cycle(graph, start, edges_count):
    """Hierholzer’s algorithm: retorna um ciclo Euleriano"""
    stack = [start]
    path = []
    used = defaultdict(int)

    while stack:
        u = stack[-1]
        while graph[u] and used[(u, graph[u][-1])] > 0:
            graph[u].pop()
        if graph[u]:
            v = graph[u].pop()
            used[(u, v)] += 1
            used[(v, u)] += 1
            stack.append(v)
        else:
            path.append(stack.pop())
    path.reverse()
    return path

def resolver(arquivo):
    with open(arquivo, "r") as f:
        dados = f.read().strip().splitlines()

    T = int(dados[0])
    idx = 1
    resultados = []

    for caso in range(1, T+1):
        N = int(dados[idx]); idx += 1
        graph = defaultdict(list)
        grau = defaultdict(int)
        beads = []

        for _ in range(N):
            a, b = map(int, dados[idx].split())
            idx += 1
            beads.append((a, b))
            graph[a].append(b)
            graph[b].append(a)
            grau[a] += 1
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
            usados = {x for x in grau if grau[x] > 0}
            if visitados != usados:
                possivel = False

        resultados.append(f"Case #{caso}")
        if not possivel:
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
    print(resolver("C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-9.2\\entrada1.txt"))
