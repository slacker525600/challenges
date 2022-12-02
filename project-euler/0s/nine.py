a = 1
b = 1
c = 1

foundsol = 0

while a <= 333 and foundsol == 0:
    b = a 
    while 2*b <= 1000 - a and foundsol == 0:
        c = 1000 - (b + a)
        #print (a,b,c)
        if a*a + b*b == c*c:
            foundsol = 1
        b += 1
    a += 1
a -= 1
b -= 1

print (a,b,c)
print (a*b*c)
