



def matrix_multiply(A,B):
    result = []
    for i in range(len(B[0])):
        result.append([0]*len(A))
    
    if len(A[0]) != len(B):
        return -1
    else:
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    result[i][j] = result[i][j] + A[i][k]*B[k][j]
                    #print('i:{}|j:{}|result|{}'.format(i, j, result[i][j]))

    return  result



if __name__ == '__main__':
    A = [
        [9, 2, 3],
        [1, 2, 3],
    ]
    B = [
        [1, 2],
        [1, 2],
        [1, 2],
    ]
    print(matrix_multiply(A, B))