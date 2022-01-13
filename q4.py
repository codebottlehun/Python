# Q4 Answer Template
from functools import reduce

def GCD(a, b):
    '''
    Euclid's Algorithm
    Condition : The first parameter must be larger than second.
    '''
    while b:
        a, b = b, a % b
    return a

def solution(arr):
    answer = int(reduce(lambda a, b : a * b / GCD(a, b), arr))
    return answer

arr = [None]*15
arr = [2,6,8,14]
answer = solution(arr)
print(answer)
