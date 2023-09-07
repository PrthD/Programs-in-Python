def calcX(x):
    assert(x)>0
    upper = max(x,1)
    lower = min(x,1)
    assert(upper>lower) # This assert is new
    while True:
        estimate = (lower+upper)/2
        assert (upper>lower) # This assert is new
        if upper-lower<0.0001:
            return estimate
        elif estimate+2 > x:
            upper = estimate
        else:
            lower = estimate

 

    

#run its
print(calcX(4))