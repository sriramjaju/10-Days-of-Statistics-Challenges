a = int(input())
b = sorted(list(map(int, (input()).split(' '))))

#print(a, b)

    

def median(sorted_list):
    #print(sorted_list)
    if len(sorted_list)%2 != 0:   #if len is odd
        return sorted_list[len(sorted_list)//2]
    else:
        return (sorted_list[len(sorted_list)//2-1] + sorted_list[(len(sorted_list)//2)])//2
    
def quantiles(sort_list):
    Q1 = median(sort_list[:len(sort_list)//2])
    Q2 = median(sort_list)
    if len(sort_list)%2 == 0:
        Q3 = median(sort_list[len(sort_list)//2:])
    else:
        Q3 = median(sort_list[len(sort_list)//2+1:])
    print(Q1)
    print(Q2)
    print(Q3)
    #return Q1, Q2, Q3

quantiles(b)
