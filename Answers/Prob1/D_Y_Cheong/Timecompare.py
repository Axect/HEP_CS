def sum_code1(x):
    return(forsum(1000000))
    
def forsum(x):
    sum = 0
    for i in range(1,1000001):
        sum = sum + i
    
    return sum

def numpysum(x):
    x = range(1,1000001)
    return np.sum(x)

%timeit sum_code1(x)
%timeit numpysum(x)