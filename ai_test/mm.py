values = [3,5,6,9,1,2,0,-1]
second = []
flag = True
for i in range(3):
    for j in range(0,len(values),2):
        if flag:
            a = max(values[j], values[j+1])
        else:
            a = min(values[j], values[j+1])
        second.append(a)

    if flag:
        flag = False
    else:
        flag = True

    values.clear()
    values = list(second)
    second.clear()


print(values)
