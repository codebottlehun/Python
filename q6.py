# Q6 Answer template

def solution(arr):
    arr.remove(min(arr))
    if not len(arr): arr.append(-1)
    return arr

arr = [4, 3, 2, 1]
#arr = [10]
answer = solution(arr)
print(answer)
