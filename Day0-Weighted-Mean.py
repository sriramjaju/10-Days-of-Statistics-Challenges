N = int(input())
data = list(map(int, input().split(' ')))
weights = list(map(int, input().split(' ')))

sum_weights = 0
for weight in weights:
    sum_weights = sum_weights + weight
    
sum_wdata = 0
for i, j in zip(data, weights):
    sum_wdata = sum_wdata +(i*j)

w_mean = sum_wdata/sum_weights

print(round(w_mean, 1))
