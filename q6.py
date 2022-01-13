# Q6 Answer template

def solution(arr):
    idx = arr.index(min(arr))
    li = []
    for i, a in enumerate(arr):
        if i == idx: continue
        li.append(a) 

    if not len(li): li.append(-1)
    return li

arr = [4, 3, 2, 1]
#arr = [10]
answer = solution(arr)
print(answer)