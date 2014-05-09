x = 1
y = 2
z = x + y
set = []
evens = []

while y < 4000000: ##this is a bad hack; doesn't work with z, but does with y and x; couldn't figure out how to use all three
    set.append(x)
    set.append(y)
    set.append(z)
    x = z + y
    y = x + z
    z = x + y
    
for i in set:
    if i % 2 == 0:
        evens.append(i)

print sum(evens)