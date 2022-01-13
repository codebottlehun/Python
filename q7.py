# Q7 Answer Template

def solution(arr):
    answer = [arr[0]]
    arr = arr[1:]
    
    for a in arr:
        if answer[-1] != a: answer.append(a) 
        
    return answer

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)
