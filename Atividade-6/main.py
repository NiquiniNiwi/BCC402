def factorial(value:int): #Calculo fatorial geral n!
    if value <= 1: #Caso base
        return 1
    return value * factorial (value - 1) #chamada recursiva da função

def HMPL(value:int): #O Calculo base para quantos pedaços de terra existem é HMPL = 1 + (n!/2!(n-2)!) + (n!/4!(n-4!))
    n_fac = factorial(value) #Calculo no N!
    k_2 = factorial(2) * factorial(value - 2) if value > 1 else 1000000 #Caso n < k a etapa é ignorada, dividindo por um numero muito grande pro resultado ser irrelevante.
    k_4 = factorial(4) * factorial(value - 4) if value > 3 else 1000000 #Caso n < k a etapa é ignorada, dividindo por um numero muito grande pro resultado ser irrelevante.
    #k_6 = factorial(6) * factorial(value - 6) if value > 7 else 1000000
    #return round(1 + (n_fac/k_2) + (n_fac/k_4) + (n_fac/k_6))
    return round(1 + (n_fac/k_2) + (n_fac/k_4)) #Calculo final
    '''
        Honestamente fiquei um pouco confuso quando fui pesquisar sobre o problema.
        Não estava entendendo muito a formula aplicada, particularmente o porque de para em k = 4.
        Quando pesquisei mais e mais achei duas formalas, a implementada e uma que usa k = 6 também.
        Deixei ambos aqui no codigo, o com k = 6 comentado.
    '''

def process_lines(filename):
    results = []
    with open(filename, 'r') as file:
        lines = file.read().split('\n')#Lendo arquivo de entrada splitando no ENTER
    idx = 0 #index para as linhas da entrada
    num_cases = int(lines[idx])
    idx+=1

    for _ in range(num_cases):
        value = lines[idx].strip() #Apend linha a linha
        idx += 1
        value = int(value)
        results.append(HMPL(value))

    for result in results:
        print(f'{result}')


for i in range(1):
    print(f'--- ENTRADA {i+1} ---')
    process_lines(f'C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-6\\entrada{i+1}.txt')
    print("------------------")