prev1 = 1
prev2 = 0

print("Fibonacci Series:")
print(prev2)
print(prev1)

for i in range(18):
    next_fibonacci = prev1 + prev2
    print(next_fibonacci)
    prev2 = prev1
    prev1 = next_fibonacci
    