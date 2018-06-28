# Finding Bell Number using Summation of Sterling's Numbers
             
def Sterling(N, k):
    if n == 0 or k == 0 or k > n:
        return 0
    if k == 1 or n == k:
        return 1
    else :
        return k*Sterling(N-1, k) + Sterling(N-1, k-1)
    
def BellNumbers(N):
    PARTITIONS = 1
    for i in range(N):
        PARTITIONS += Sterling(N,i)
    return PARTITIONS
        
        
    # Utility code to test this BellNUmbers function:
main_set = list(map(int,input().split()))
    
print ("There are {} ways to split the set : {} into disjoint sets".format(BellNumbers(len(main_set)), main_set))
