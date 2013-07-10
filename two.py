def fib(last, onebefore):
    if(last + onebefore > 4000000):
        return 0
    elif((last + onebefore )%2 == 1):
        return fib(last + onebefore , last)
    else:
        return last+onebefore + fib(last + onebefore , last)

print (fib(1,1))
