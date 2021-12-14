A = input()
B = int(input())
array_list = []
for i in range(0, B):
    i = input()
    array_list.append(i)
max_avr = max_idx = 0
for i in range(B):
    L = A.count("L") + array_list[i].count("L")
    O = A.count("O") + array_list[i].count("O")
    V = A.count("V") + array_list[i].count("V")
    E = A.count("E") + array_list[i].count("E")

    avr = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if max_avr < avr:
        max_avr = avr
        max_idx = i

print(array_list[i])
