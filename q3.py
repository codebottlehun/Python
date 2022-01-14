def solution(arr, divisor):
    answer = list(filter(lambda x: x % divisor == 0, arr))
    return answer if len(answer) > 0 else [-1]

arr = [5, 9, 7, 10]
divisor = 5
answer = solution(arr, divisor)
print(answer)