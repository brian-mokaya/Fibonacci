prev1 = 0
prev2 = 1

print("Fibonacci Series:")
print(prev1)
print (prev2)

for i in range(18):
    next_fibonacci = prev1 + prev2
    print(next_fibonacci)
    prev1 = prev2
    prev2 = next_fibonacci
    