

def longest_common_seq_length(A, B):
    matrix = []
    len_A = len(A)
    len_B = len(B)
    #print('Length of String A : {}'.format(len_A))
    #print('Length of String B : {}'.format(len_B))
    for i in range(len_B + 1):
        matrix.append([0]*(len_A+1))

    for i in range(1,len_B+1):
        for j in range(1,len_A+1):
            #print('i:{} and j:{} / {} and {}'.format(i, j, B[i-1], A[j-1] ))
            if A[j-1] == B[i-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1] 
            else:
                matrix[i][j] = max( matrix[i-1][j], matrix[i][j-1] )


    #for i in range(len_B + 1):
    #    print(matrix[i])
    
    return matrix[len_B][len_A]


if __name__ == '__main__':
    print('Starting')
    string_1 = 'ACDE'
    string_2 = 'ABCADA'
    length = longest_common_seq_length(string_1, string_2)
    print('LCS Length : {}'.format(length))