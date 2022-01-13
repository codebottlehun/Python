def solution(store, customer):
    store_mask = {}
    for v in store:
        store_mask[v] = True
    
    answer = []
    for v in customer:
        answer.append('yes' if store_mask.get(v, False) else 'no')
    
    
    return answer

store = [2,3,7,8,9]
customer = [7,5,9]
answer = solution(store, customer)
print(answer)