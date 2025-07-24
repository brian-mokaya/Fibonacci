print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        next_fibonacci = prev1 + prev2
        print(next_fibonacci)
        prev1 = prev2
        prev2 = next_fibonacci
        count += 1

        fibonacci(prev1, prev2)
    else:
        return 
    
fibonacci(0, 1)