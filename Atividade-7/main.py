import sys
import math
import random

def is_prime(n: int) -> bool:
    if n < 2: #1 é irrelevante
        return False
    if n % 2 == 0: #O unico numero par primo é 2
        return n == 2
    '''
    Quando queremos saber se um número n é primo, a ideia é verificar se ele tem algum divisor além de 1 e dele mesmo.
    Se n não for primo (ou seja, for composto), então ele pode ser escrito como n = a × b.
    Nesse caso, pelo menos um dos fatores a ou b é menor ou igual a √n. 
    '''
    r = int(math.isqrt(n)) 
    for d in range(3, r + 1, 2):
        if n % d == 0: #checa o resto da divisão de 
            return False
    return True

def is_carmichael(n: int) -> bool:  
    if is_prime(n): 
        return False
    # Fermat congruence for all a coprime to n, 2 <= a <= n-1
    for a in range(2, n):
        if math.gcd(a, n) == 1:
            '''
            pow(a,n,m) = (a^n) mod m
            O Pequeno Teorema de Fermat (adaptado para Carmichael) diz:
            Se n é primo (ou Carmichael), então para todo a coprimo de n:
            𝑎^𝑛 ≡ 𝑎(mod 𝑛) em python pow(a, n, n) == a % n
            Se encontrar um caso onde não vale (!=), então N não é Carmichael 
            '''
            if pow(a, n, n) != a % n:
                return False
    return True

def resolver(arquivo):
    with open(arquivo, "r") as f:
        dados = f.read().strip().splitlines()

    idx = 0
    nao_zero = True
    while nao_zero:
        if int(dados[idx]) == 0:
            nao_zero = False
        elif int(dados[idx])  < 3 or int(dados[idx])  >= 65000:#A entrada tem que ser maior que 2 e menor que 65000
            print("Number out of range")
        elif is_carmichael(int(dados[idx])):
            print(f"The number {dados[idx]} is a Carmichael number.")
        else:
            print(f"{dados[idx]} is normal.")
        idx+=1

if __name__ == "__main__":
    n = random.randint(1,3)
    print(f"Entrada {n}")
    resolver(f"C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-7\\entrada{n}.txt")


'''
Números de Carmichael

Um número de Carmichael é um número composto (ou seja, não é primo) que consegue enganar o teste de primalidade de Fermat.

O teste de Fermat diz que, se p é primo e a é um número inteiro tal que gcd(a,p) = 1, então:

a^p ≡ a (mod p)

Para a maioria dos números compostos, essa congruência falha para algum valor de a.
Mas, para os números de Carmichael, ela funciona para todo a coprimo com n.
Isso faz com que eles pareçam primos quando, na verdade, não são.

---

Exemplo: 561

* 561 = 3 x 11 x 17, então é composto.
* No entanto, para qualquer a que seja coprimo com 561, vale:

a^561 ≡ a (mod 561)

Isso significa que o número 561 passa sempre no teste de Fermat, mesmo não sendo primo.
Por isso, 561 é o menor exemplo clássico de número de Carmichael.
'''