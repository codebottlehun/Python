# Q5 Answer template
def twosum(li, target):
    left, right = 0, len(li)-1
    result = []
    while left < right:
        sum = li[left] + li[right]
        if sum == target: 
            result.append((li[left], li[right]))
            left += 1
        elif sum > target: right -= 1
        else: left += 1
    return result

def solution(n, s):
    li = twosum([i for i in range(1, s+1)], s)
    if len(li) == 0 : return -1
    
    li_multi = [a*b for a, b in li]
    idx = li_multi.index(max(li_multi))
    
    answer = list(li[idx])
    return answer

n = 2
s = 9
answer = solution(n, s)
print(answer)