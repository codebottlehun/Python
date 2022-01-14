def solution(n):
    li = [0, 1]
    
    for i in range(2, n+1):
        num = li[i - 1] + li[i - 2]
        li.append(num)

    return li[n]

answer = solution(20)
print(answer)






