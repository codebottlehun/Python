# Q2 Answer template
from itertools import combinations

def solution(numbers):
    li = list(combinations(numbers, 2))
    return sorted(list({a+b for a, b in li}))

numbers = [2,1,3,4,1]
answer = solution(numbers)
print(list(answer))