def lis():
    n = int(input("Enter the length : "))
    lst = []
    for i in range(n):
        a = int(input('Enter the element : '))
        lst.append(a)
    return lst

list1 = lis()
list2 = lis()

union = list(set(list1) | set(list2))
intersecion = list(set(list1) & set(list2))

print(union)
print(intersecion)
