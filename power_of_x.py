def power(x,n):
    if n == 1:
        return x
    if n % 2 == 0:
        return power(x,n//2) * power(x,n//2)
    else:
        return power(x,n//2) * power(x,n//2) * x
print(power(3,5))