from collections import Counter

# Mapeamento de valores para facilitar a ordenação
CARD_VALUES = {r: i for i, r in enumerate('23456789TJQKA', start=2)}

# Classificação das mãos (quanto maior o número, melhor a mão)
RANK_ORDER = {
    'high_card': 1,
    'pair': 2,
    'two_pair': 3,
    'three': 4,
    'straight': 5,
    'flush': 6,
    'full_house': 7,
    'four': 8,
    'straight_flush': 9,
}

def hand_rank(hand):
    values = sorted([CARD_VALUES[card[0]] for card in hand], reverse=True)
    suits = [card[1] for card in hand]

    val_count = Counter(values)
    val_freq = sorted(val_count.items(), key=lambda x: (-x[1], -x[0])) #Frequancias de cada VALOR de carta na mão, ordenado por quantidade cards. Ex: 2C 2D 4S 4C 2S o valor ficar [(2,3),(4,2)] 
    ordered_values = [v for v, count in val_freq for _ in range(count)] #Valores ordenados na mão. EX: 2C 2D 4S 4C 2S o valor ficar [4, 4, 2, 2, 2]

    is_flush = len(set(suits)) == 1 # Contabiliza a quantidade de suits(naipes) diferentes em uma mão. Se 1, é flush
    is_straight = values == list(range(values[0], values[0]-5, -1)) #Valida se a ordenação é sequencial. Se sim, é straight
    
    '''
    BREVE EXPLICAÇÂO DO PORQUE USAR TUPLAS PARA COMPARAÇÃO
    EX:
    (3, 5, 2) > (3, 5, 1)   # True
    (3, 5, 2) < (3, 6, 0)   # True
    (3, 5, 2) == (3, 5, 2)  # True
    (3, 5, 2) < (3, 5, 2, 1) # True
    
    Compara o primeiro elemento de cada tupla.
    Se forem iguais, compara o segundo.
    Continua até achar uma diferença.
    Se uma tupla for prefixo da outra, a mais curta é menor.
    '''

    if is_straight and is_flush: #Se straight e flush, melhor mão
        return (RANK_ORDER['straight_flush'], values[0])
    elif val_freq[0][1] == 4: #Se four of a kind, nossa quadra. Ex: 2C 2D 2H 9C 2S
        return (RANK_ORDER['four'], val_freq[0][0], val_freq[1][0])
    elif val_freq[0][1] == 3 and val_freq[1][1] == 2: #Se full house. Ex: 2C 2D 4S 4C 2S o valor ficar [(2,3),(4,2)]
        return (RANK_ORDER['full_house'], val_freq[0][0], val_freq[1][0])
    elif is_flush: #Se flush
        return (RANK_ORDER['flush'], *values)
    elif is_straight: #Se straight
        return (RANK_ORDER['straight'], values[0])
    elif val_freq[0][1] == 3: #Se tree of a kind, nossa trinca. 2C 2D 4S 8C 2S o valor ficar [(2,3),(8,1),(4,1)]
        return (RANK_ORDER['three'], val_freq[0][0], *ordered_values)
    elif val_freq[0][1] == 2 and val_freq[1][1] == 2: #Two pair, dois pares. EX: 2C 9D 4S 4C 2S o valor ficar [(4,2),(2,2),(9,1)]
        high_pair = max(val_freq[0][0], val_freq[1][0]) #Maior par da mão
        low_pair = min(val_freq[0][0], val_freq[1][0]) #Menor par da mão
        kicker = val_freq[2][0] #Carta que sobra, em caso de empates dos pares é relevante
        return (RANK_ORDER['two_pair'], high_pair, low_pair, kicker) # Importante para desempate
    elif val_freq[0][1] == 2:
        return (RANK_ORDER['pair'], val_freq[0][0], *ordered_values) # Par e resto, resto é usado para desempate
    else:
        return (RANK_ORDER['high_card'], *values) #High card

def compare_hands(line):
    cards = line.strip().split()
    black = cards[:5]
    white = cards[5:]
    rank_black = hand_rank(black)
    rank_white = hand_rank(white)

    if rank_black > rank_white: # Comparação das tuplas, essa comparação ser de tuplas é importante pra comparar "o conjunto", isso é pra evitar empates.
        return "Black wins."
    elif rank_white > rank_black:
        return "White wins."
    else:
        return "Tie."

# Leitura de um arquivo com várias linhas de mãos
def process_input_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            try:
                if line.strip(): # Manda linha a linha até as linhas se acabarem ou dar um erro.
                    print(compare_hands(line))
            except:
                print('Erro na leitrua da linha.')


for i in range(5):
    print(f'--- ENTRADA {i+1} ---')
    process_input_file(f'C:\\Users\\TEC\\Desktop\\BCC402\\Atividade-2\\poker_input_{i+1}.txt')
    print("------------------")