import math

N = int(input())
data = list(map(int, input().split(' ')))

#print(N, data)
total = 0
for i in data:
    total = total + i
mean = total/N

squared_sum = 0
for j in data:
    squared_sum = squared_sum + (j - mean)**2
    
std_dev = math.sqrt(squared_sum/N)

print(std_dev)
