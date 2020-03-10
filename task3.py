def number():
    n = int(input('Введите число:' ))
    return('число %s  следуюший число %s,число %s предедущий %s '%(str(n),str(n+1),str(n),str(n-1)))
print(number())