n = int(input())
num = list(map(int, [input() for _ in range(n)]))
dentro = fora = 0
for i in range(n):
    if 10 <= num[i] <= 20:
        dentro = dentro+1
    else:
        fora = fora+1
print(dentro,' in\n',fora,' out',sep = '')
