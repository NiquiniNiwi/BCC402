def check_palindrome(value):
    len_value = len(value) #Pega o Tamanho do "numero"
    for i in range(len_value):
        if value[i] != value[len_value-1-i] and i <= len_value-1-i: #Se em qualquer momento a comparação for diferente, não é palindromo e retorna. Para depois da metade de maneira forçada.
            return False
    return True

def RaA(value):
    sum = 0 #inicia quantidade de somas necessarias para ser palindromo
    result = str(value) #copia valor inicial como string
    while not check_palindrome(result): #envia o valor para avaliar se é palindromo, se for retorna.
        if sum >= 1000: #Caso de 1000+ somas deve não fazer
            return ['Not', 'Computable']
        if int(result) > 4294967295: #caso do valor ser maior que 4294967295 não deve ser avaliado.
            return ['Too big', 'of a number']
        r_value = result[::-1] #inverte o valor (isso é do proprio python, mas como estamos trablahando com strings da pra fazer isso na mão)
        sum+=1 #+1 pra cada soma executada
        result = str(int(r_value) + int(result)) #soma numero com seu inverso ex: 21 + 12
    return [sum, result]


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
        results.append(RaA(value))

    for result in results:
        print(f'{result[0]} {result[1]}')


for i in range(5):
    print(f'--- ENTRADA {i+1} ---')
    process_lines(f'C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-5\\entrada{i+1}.txt')
    print("------------------")