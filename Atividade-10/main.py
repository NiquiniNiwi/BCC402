import random

def count_subsequences(X, Z):
    m, n = len(X), len(Z) #Tamnhos da string e da substring
    dp = [0] * (n + 1)
    dp[0] = 1  # subsequência vazia sempre existe

    for i in range(1, m + 1):
        for j in range(n, 0, -1):  # percorre de trás pra frente
            '''
            Isso é importante: se percorresse da frente pra trás, a atualização sobrescreveria valores de dp[j-1] que ainda serão usados no mesmo passo.
            Indo de trás para frente, garantimos que cada estado dp[j] só usa o valor de dp[j-1] da iteração anterior (sem interferir).
            '''
            if X[i - 1] == Z[j - 1]:
                dp[j] += dp[j - 1]
                '''
                Se o caractere atual de X (X[i-1]) for igual ao caractere atual de Z (Z[j-1]):
                Podemos usar esse caractere de X para formar uma subsequência de comprimento j.
                O número de novas subsequências formadas é exatamente dp[j-1] (todas as formas de formar a subsequência de tamanho j-1).
                Então somamos: dp[j] += dp[j-1].
                '''
    return dp[n]

def resolver(arquivo):
    # leitura do arquivo
    with open(arquivo, "r") as f:
        lines = f.read().splitlines()

    T = int(lines[0])  # número de casos
    idx = 1
    for _ in range(T):
        X = lines[idx].strip() #String
        Z = lines[idx + 1].strip() #substring que queremos
        idx += 2
        print(count_subsequences(X, Z))

if __name__ == "__main__":
    n = random.randint(1,5)
    print(f"Entrada {n}")
    resolver(f"C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-10\\entrada{n}.txt")