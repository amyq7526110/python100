#!/usr/bin/env python3

def fibo(x):
    fib = [ 0, 1 ]
    for i in range(x):
         fib.append(fib[-1] + fib[-2])
    print(fib)
if __name__ == '__main__':
    fibo(15)


