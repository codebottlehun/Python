def solution(k, a, b):
    for i in range(k):
        mi = min(a)
        ma = max(b)
        
        a[a.index(mi)] = ma
        b[b.index(ma)] = mi
    
    return sum(a)

k = 3
a, b = [1,2,5,4,3], [5,5,6,6,5]
#a = [1,2,5,4,3]
#b = [5,5,6,65]
answer = solution(k, a, b)
print(answer)