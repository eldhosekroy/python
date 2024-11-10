def matmul(mat1,mat2):
    if len(mat1[0]) != len(mat2):
        print("Matrix can't be multiple")
        return
    
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

mat1 = [
    [1,2,3],
    [1,2,3]
    ]
mat2 = [
    [1,1],
    [2,2],
    [3,3]
    ]

result = matmul(mat1,mat2)

if result:
    print('Matrix Multi is')
    for row in result:
        print(row)
