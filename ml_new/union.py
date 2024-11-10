list1 = [1,2,4,6,7]
list2 = [9,5,2,1,5]

union = list(set(list1) | set(list2))
intersection = list(set(list1) & set(list2))

print(f'List1 : {list1}')
print(f'List2 : {list2}\n')

print(f'Union : {union}')
print(f'Intersection : {intersection}')
