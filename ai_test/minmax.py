values = [3,5,6,9,1,2,0,-1]
second = []
alpha = float('-inf')
beta = float('inf')
flag = True

for i in range(3):
    for j in range(0, len(values), 2):
        if flag:
            a = max(values[j], values[j+1])
            alpha = max(alpha, a)
        else:
            a = min(values[j], values[j+1])
            beta = min(beta, a)
        second.append(a)
        
        if beta <= alpha :
            break

    flag = not flag

    values.clear()
    values = list(second)
    second.clear()
    alpha, beta = float('-inf'),float('inf')

print(f'Optmial value : {values[0]}')

