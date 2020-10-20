def split_ascii(s):
    return [ch for ch in s]
n = 0
while True: 
    try:
        contagem = {}
        entrada = list(map(ord, (split_ascii(input()))))
        for element in entrada:
            if element in contagem:
                contagem[element] += 1
            else:
                contagem[element] = 1
        ordem = dict(sorted(contagem.items(), key=lambda x: (x[1], -x[0])))
        n += 1
        if n > 1: print()
        for key, value in ordem.items():
            print(f"{key} {value}")
    except EOFError:
       break
