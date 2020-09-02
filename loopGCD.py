def computeGCD(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd


a = int(input("Enter first number: "))
b = int(input("Enter second number "))
c = str("%s,%s" % (a, b))
d = str(computeGCD(a, b))
print("gcd(" + c + ") = " + d)