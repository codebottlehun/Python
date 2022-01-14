# Q0 Answer template

"""
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
"""
n = 4
data = [1, 3, -2, 2]


def average(data):
    return int(sum(data) / len(data))

def middleValue(data):
    tmp = sorted(data)
    return tmp[int(len(tmp)/2)]

def greatestCnt(data):
    st = set(data)
    dic = {}
    for a in st: dic[a] = 0
    for a in data: dic[a] += 1
    
    largestValue = max(dic.values())
    for key, value in dic.items():
        if value == largestValue:
            return key
    
    return -1

def condi4(data):
    return max(data) - min(data)

print(average(data))
print(middleValue(data))
print(greatestCnt(data))
print(condi4(data))