#Matriz de possiveis direções
directions = [(-1, -1), (-1, 0), (-1, 1),
              ( 0, -1),          ( 0, 1),
              ( 1, -1), ( 1, 0), ( 1, 1)]

#Função recursiva para achar palavra palavra
def verify_word(word, matrix, x, y, dx, dy, init):
    i,j = x + init * dx, y + init * dy #Calculo para quantas vezes na direção estamos indo, isso é baseado na posição atual somada ao direcional vezes o numero de movimentos que falta.
    if (not (0 <= i < len(matrix) and 0 <= j < len(matrix[0]))): #Caso para parar se posição é invalída.
        return 0
    if word and (word[0] == matrix[i][j]): #Se primeira letra da plavra de entrada bate com a posição avaliada.
        return 1 + verify_word(word[1:], matrix, i,j, dx,dy, len(word) - len(word[1:])) #Passa palavra sem a letra já avaliada, posição atual(geral), direção e quantas vezes vai ir para a proxima direção 
    elif not word: #Se palavra vazia
        return 0
    else: #Caso base
        return 0

#Função "principal"
def where_is_waldorf(words, input_matrix, n, m):
    result_M = [] #resultado da matriz
    for word in words: #Para todas as palavras
        result_w = [] #resultado da palavra
        for x,y in directions: #Para cada direção possivel: ↖, ↑, ↗, ←, →, ↙, ↓, ↘
            for i  in range(n): #Linhas da matriz
                for j in range(m): #Colunas da matriz
                    #Chamada inicial com a palavra, a matriz, as posições iniciais, o direcionais e o a quantidade inicial de movimentos na direção
                    if len(word) == verify_word(word, input_matrix, i, j, x, y, 0): 
                        result_w = [i+1,j+1, word] # index + 1
        if not result_w: #Não é necessairo se realmente todas as palavras existem no grid, como o problema propoem
            result_w = [-1,-1, word] #Not found kekw
        result_M.append(result_w)
    return result_M

def process_lines(filename):
    results = []
    with open(filename, 'r') as file:
        lines = file.read().split('\n')#Lendo arquivo de entrada splitando no ENTER
    idx = 0 #index para as linhas da entrada
    num_cases = int(lines[idx])
    idx+=1

    for _ in range(num_cases):
        # Pula linha em branco entre casos
        while idx < len(lines) and lines[idx].strip() == '':
            idx += 1
        m, n = map(int, lines[idx].split()) #Pega o tamanho da matriz de letras
        idx += 1

        input_matrix = [] #Inicialização da matriz de letras
        for _ in range(m):
            input_matrix.append(lines[idx].strip()) #Apend linha a linha
            idx += 1

        number_of_words = int(lines[idx]) #Numeor de palavras pra encontrar na matriz
        idx += 1

        words = []
        for _ in range(number_of_words):
            words.append(lines[idx].strip()) #Apeende de todas as palavras
            idx += 1

        results.append(where_is_waldorf(words, input_matrix, len(input_matrix), len(input_matrix[0]))) #Chamada da função principal
        idx += 1

    for result in results:
        print('')
        for r in result:
            print(f'{r[0]} {r[1]}')

for i in range(5):
    print(f'--- ENTRADA {i+1} ---')
    process_lines(f'C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-3\\entrada{i+1}.txt')
    print("------------------")