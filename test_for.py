v = [None]*10
v[0] = 0
for i in range(1, len(v)):
    v[i] = v[i-1]+1

print(v)