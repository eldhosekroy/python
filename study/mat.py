def mat(mat1,mat2):
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def val():
    row1 = int(input("Enter row1 :"))
    col1 = int(input("Enter col1 : "))
    row2 = int(input("Enter row2 : "))
    col2 = int(input("Enter col2 : "))

    if col1 != row2:
        print("Matrix mulitplication can't done")
        return

    print("Matrix 1")
    mat1 = [[0 for _ in range(col1)] for _ in range(row1)]
    mat2 = [[0 for _ in range(col2)] for _ in range(row2)]
    for i in range(row1):
        for j in range(col1):
            mat1[i][j] = int(input(f"Enter element at {i} {j}"))

    print('Matrix 2')
    for i in range(row2):
        for j in range(col2):
            mat2[i][j] = int(input(f"Enter element at {i} {j}"))
              
    return mat(mat1,mat2)
val = val()
print(val)
