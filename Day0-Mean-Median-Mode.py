import numpy as np
a = int(input())
b = input()

b1 = b.split(' ')

results = list(map(int, b1))
arr = np.array(results)

    
print(arr.mean())
print(np.median(arr))
counts = np.bincount(arr)
print (np.argmax(counts))
