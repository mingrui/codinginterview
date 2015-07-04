# remember O(2^n) is the runtime complexity
# with memoize, O(n) runtime and O(n) space if recursive
# with memoize and bottom-up O(n) runtime and O(1) space

# hash the results

def fib(n, fibDict):
    if n in fibDict:
        return fibDict[n]
    
    if n == 0:
        fibDict[0] = 0
        return 0
    elif n == 1:
        fibDict[1] = 1
        return 1
    else:
        result = fib(n-1, fibDict) + fib(n-2, fibDict)
        fibDict[n] = result
        return result

# better to warp function in a class

# SOLUTION 2
# bottom up with memoize
def BottomUpFib(n):
    if n < 0:
        raise Exception("error: n < 0")
        
    if n in [0, 1]:
        return n
    
    prevPrev = 0
    prev = 1
    for index in range(n-1):
        current = prevPrev + prev
        prevPrev = prev
        prev = current
        
    return current
        
print BottomUpFib(6)
    
    
    
    
    
    
    
   

















    
    
    
    
    