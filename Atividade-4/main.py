def pancake_sort(stack):
    flips = []                 # Lista para armazenar a sequência de flips realizados
    n = len(stack)             # Número total de panquecas na pilha

    # Vamos posicionar da maior panqueca até a segunda menor
    for size in range(n, 1, -1):  # size vai de n até 2 (inclusive)
        #print(f'size: {size}')
        # Encontrar a posição da maior panqueca na parte não ordenada da pilha
        max_index = stack.index(max(stack[:size]))
        #print(f'max_index: {max_index}')
        # Se essa maior panqueca não estiver na posição correta (fundo do sub-stack)
        if max_index != size - 1:
            # Se a maior panqueca não estiver no topo ainda, traz ela para o topo
            if max_index != 0:
                flips.append(n - max_index)  # Flip na posição correspondente (conforme enunciado)
                stack[:max_index + 1] = reversed(stack[:max_index + 1])  # Inverter até a posição max
                print(f'stack: {stack}')

            # Agora trazemos a panqueca do topo para sua posição correta no sub-stack
            flips.append(n - size + 1)       # Flip até a base da subpilha
            stack[:size] = reversed(stack[:size])  # Inverter as primeiras `size` panquecas
            print(f'stack: {stack}')

    flips.append(0)  # Indicador de fim da sequência de flips
    return flips     # Retorna a sequência de flips

def process_lines(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()        # Remove espaços extras e quebras de linha
            if not line:
                continue               # Ignora linhas vazias

            # Transforma a linha em uma lista de inteiros (a pilha de panquecas)
            stack = list(map(int, line.split()))
            original = ' '.join(map(str, stack))  # Guarda a pilha original como string para impressão

            # Chama o algoritmo de pancake sort (passando uma cópia da pilha)
            flips = pancake_sort(stack[:])  # stack[:] garante que a original não será modificada

            # Exibe a pilha original
            print(original)
            # Exibe a sequência de flips necessária para ordená-la
            print(' '.join(map(str, flips)))


for i in range(2):
    print(f'--- ENTRADA {i+1} ---')
    process_lines(f'C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-4\\entrada{i+1}.txt')
    print("------------------")