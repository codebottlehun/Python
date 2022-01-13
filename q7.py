# Q7 Answer Template

def solution(arr):
    answer = [arr[0]]
    
    for i, a in enumerate(arr):
        if i == 0: pass
        if answer[-1] != a: answer.append(a) 
        
    return answer

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)