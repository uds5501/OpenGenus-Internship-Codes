# Finding Bell Number using Dobinski's Formula
         
import math
         
def BellNumbers(N):
    ITERATIONS = 1500
    ANSWER = (1/math.e) * sum([(k**N)/(math.factorial(k)) for k in range(iterations)])
    return ANSWER
              
    # Utility code to test this BellNumbers function:
    main_set = list(map(int,input().split()))
    
    print ("There are {} ways to split the set : {} into disjoint sets".format(BellNumbers(len(main_set)), main_set))
