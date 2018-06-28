# Finding Bell Number using Peirce's Triangle
            
def ShowMatrix(matrix):
    for i in matrix:
        print(*i)    
        
def BellNumbers(N, show=True):
    matrix = [[0 for i in range(N+1)] for j in range(N+1)]
    matrix[0][0] = 1

    for i in range(1, N+1):
        matrix[i][0] = matrix[i-1][i-1]

        for j in range(1, i+1):
            matrix[i][j] = matrix[i-1][j-1] + matrix[i][j-1]
        if show == True:
            print("\n")
            for k in matrix:
                print (*k)

    return (matrix[N][0])
    
    
# Utility code to test this BellNUmbers function:
main_set = list(map(int,input().split()))

print ("There are {} ways to split the set : {} into disjoint sets".format(BellNumbers(len(main_set), show=False), main_set))