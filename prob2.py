i = 0
j = 1
fib = 0
suma = 0
while fib < 4000000:
    fib = i+j
    suma += fib if fib % 2 == 0 else 0
    i = j
    j = fib
    print(fib)
print(suma)


# answer 4613732
