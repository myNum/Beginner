primes = []
y = 2
x = 600851475143

while y < 13195:
    if x % y == 0:
        primes.append(y)
        x = x / y
    else:
        y = y+1
        

print max(primes)