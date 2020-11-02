# ======================== Funções do código ==============================

def sqrt(n):
    return n**0.5

def dot(v,w):
    x,y = v
    X,Y = w
    return x*X + y*Y

def length(v):
    x,y = v
    return sqrt(x*x + y*y)

def vector(b,e):
    x,y = b
    X,Y = e
    return (X-x, Y-y)

def unit(v):
    x,y = v
    mag = length(v)
    return (x/mag, y/mag)

def distance(p0,p1):
    return length(vector(p0,p1))

def scale(v,sc):
    x,y = v
    return (x * sc, y * sc)

def add(v,w):
    x,y = v
    X,Y = w
    return (x+X, y+Y)

def pnt2seg(pnt, start, end):
    # O primeiro passo é converter o segmento de reta e o ponto(que é o centro do círculo) em vetores
    seg_vec = vector(start, end)
    pnt_vec = vector(start, pnt)
    # O segundo passo é dimensionar os vetores pelo comprimento do segmento
    seg_len = length(seg_vec)
    seg_unitvec = unit(seg_vec)
    pnt_vec_scaled = scale(pnt_vec, 1.0/seg_len)
    # O terceiro passo é calcular o produto interno do vetores dimensionados, isso vai dar que se 0 < t < 1 
    # o ponto do segmento de reta mais próximo do centro do circulo está entre o ponto inicial e o
    # ponto final, caso t <= 0 o ponto mais próximo é o ponto inicial, e se t >= 1 o ponto mais próximo
    # é o ponto final
    t = dot(seg_unitvec, pnt_vec_scaled)    
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    # O quarto passo é dimensionar o vetor do segmento pelo fator 't' para encontrar a distancia minima 
    # (a partir do ponto mais próximo) entre o centro do círculo e o segmento de reta
    nearest = scale(seg_vec, t)
    dist = distance(nearest, pnt_vec)
    # O quinto passo é simplesmente deslocar o ponto mais próximo para o segmento (não é necessário para
    #  o programa funcionar mais ajuda bastante pra testar o código no geogebra)
    nearest = add(nearest, start)
    return (dist, nearest)

# ======================== Começa aqui  ========================================

T = int(input())  # Obtém o numero de casos de teste e converte a entrada para 
for _ in range(T): # Loop de entradas até o numero de casos desejado
    # Um dicionário com as magias, seus danos e raios
    magic_dic = {'fire': [200, 20, 30, 50], 'water': [300, 10, 25, 40], 'earth': [400, 25, 55, 70], 'air': [100, 18, 38, 60]}
    # Limpeza das listas só pra garantir
    dimen = []
    magic = []
    # Coloca as entradas nas listas
    dimen = list(map(int, input().split(' ')))
    magic = list(input().split(' '))
    # Construção do retângulo
    x1, y1, x2, y2 = [dimen[2], dimen[3], dimen[2]+dimen[0], dimen[3]]
    x3, y3, x4, y4 = [dimen[2]+dimen[0], dimen[3]+dimen[1], dimen[2], dimen[3]+dimen[1]]
    # Parâmetros da magia
    level, cx, cy = map(int, [magic[1], magic[2], magic[3]])
    r = magic_dic[magic[0]][level]
    # Primeiro passo verifica se o centro do círculo está dentro do retângulo,
    # se dentro do rentângulo a unidade foi atingida e o dano é exibido
    if (x1 <= cx <= x2) and (y1 <= cy <= y3):
        print(magic_dic[magic[0]][0])
    # Caso o contrário verifica a distância do centro do circulo até os segmentos de reta
    # que compõem o retângulo e seleciona a menor distância
    else:
        # o if e os dois elif seguintes são para caso w ou/e h = 0
        if (dimen[0] == 0) and (dimen[1] == 0):
            menor_dist_P = distance((cx, cy), (x1, y1))
        elif dimen[0] == 0:
            SegAD_P = pnt2seg((cx, cy), (x1, y1), (x4, y4))
            menor_dist_P = SegAD_P[0]
        elif dimen[1] == 0:
            SegAB_P = pnt2seg((cx, cy), (x1, y1), (x2, y2))
            menor_dist_P = SegAD_P[1]
        # Quando w e h =/= 0
        else:
            SegAB_P = pnt2seg((cx, cy), (x1, y1), (x2, y2))
            SegBC_P = pnt2seg((cx, cy), (x2, y2), (x3, y3))
            SegCD_P = pnt2seg((cx, cy), (x3, y3), (x4, y4))
            SegAD_P = pnt2seg((cx, cy), (x1, y1), (x4, y4))
            menor_dist_P = min(SegAB_P[0], SegBC_P[0], SegCD_P[0], SegAD_P[0])
        # Verifica se a menor distância é igual ou menor que o raio,
        # caso positivo então a unidade foi atingida
        if menor_dist_P <= r:
            print(magic_dic[magic[0]][0])
        # Caso contrário o ataque não acertou
        else:
            print('0')
