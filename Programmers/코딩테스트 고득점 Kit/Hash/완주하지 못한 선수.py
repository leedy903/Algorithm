'''
Solution 1
keyword: sort, zip 이용
'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("")
    for p, c in zip(participant, completion):
        if p != c:
            return p

'''
Solution 2 - 다른 사람의 풀이 참고
keyword: Counter 사용
'''
# from collections import Counter


# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer.keys())[0]

'''
Solution 3 - 다른 사람의 풀이 참고
keyword: hash 이용
'''
# def solution(participant, completion):
#     answer = ''
#     _hash = 0
#     dic = {}
    
#     for part in participant:
#         dic[hash(part)] = part
#         _hash += hash(part)
        
#     for com in completion:
#         _hash -= hash(com)
        
#     answer = dic[_hash]
#     return answer