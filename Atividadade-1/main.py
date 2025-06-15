#Inicialização
def process_lines(filename):
    #inicialização dos paramentros de entrada
    field_num = 0 #Nmr de campos
    n = [] #Lista de tamanho de linhas do campo
    m = [] # Lista de tamanho de colunas do campo
    field = [] #Lista de Campos
    result = [] #Lista de Saídas
    idx = 0 #Auxiliar de passagem de linhas do arquivo.

    # Esse é o trecho de codigo para input manual.
    # while True:
    #     l, c = map(int, input().split())
    #     if l == 0 and c == 0:
    #         break
    #     n.append(l)
    #     m.append(c)
    #     field.append([list(input()) for _ in range(l)])
    #     result.append([['' for _ in range(c)] for _ in range(l)])
    #     field_num+=1
    ##############################################

    with open(filename, 'r') as file:
        lines = file.read().splitlines() #Lendo arquivo de entrada

    while idx < len(lines): #Enquanto numero de linhas do arquivo não é excedido.
        l, c = map(int, lines[idx].split()) #Lê a linha que o auxiliar aponta e faz um split para lermos o tamanho do campo
        idx += 1 #ir para a proxima linha, nesse caso a primeira linha do campo
        if l == 0 and c == 0: #Se 0 0, acaba a leitura de campos.
            break
        n.append(l) #Adicionando a listagem de linhas
        m.append(c) #Adicionando a listagem de colunas

        field.append([list(lines[idx + i]) for i in range(l)]) #Lendo todas as linhas do campo e adicionando a lista de campos. Indifere do tamanho da coluna
        idx += l #Adiociona o total de linhas do compo a contagem de linha já trasitadas do arquivo.

        result.append([['' for _ in range(c)] for _ in range(l)]) #Criando campo vazio com tamanho L por C (tamanho do campo atual).
        field_num+=1
    
    for k in range(field_num): #para cada Campo existente
        for i in range(n[k]): #Para linhas do campo atual
            for j in range(m[k]): #Para colunas do campo atual
                if field[k][i][j] == '*': #avalia caso de BOMBA
                    result[k][i][j] = '*' 
                else: #Se não bomba
                    count = 0 #Inicializa contagem de bombas adjacentes.
                    for dx in [-1, 0, 1]: #Mover em todas as 3 direções possiveis no eixo X
                        for dy in [-1, 0, 1]: #Mover em todas as 3 direções possiveis no eixo Y
                            ni, nj = i + dx, j + dy #posição i e j são a posição autal, dx e dy é o movimento
                            if 0 <= ni < n[k] and 0 <= nj < m[k] and field[k][ni][nj] == '*': #avalia se a linha e coluna "existem". Valida se existe bomba ajacente.
                                count += 1
                    result[k][i][j] = str(count) #depois de avaliar todas as direções, atribui valor de bombas adjacentes.

    for i in range(field_num): #Para todos os campos
        if i > 1: #Valida se existe mais de um campo, se for o segundo ou posterior, imprime um espaço
            print()
        print(f"Field #{i+1}:") #imprime qual o campo estamos dando resultado
        for row in result[i]: #imprime cada linha do campo I
            print(''.join(row))

for i in range(5):
    print(f'--- ENTRADA {i+1} ---')
    process_lines(f'C:\\Users\\TEC\\Desktop\\BCC402\\Atividadade-1\\entrada{i+1}.txt')
    print("------------------")
