def solution(priorities, location):
    answer = 0
    while priorities:
        if priorities[0] == max(priorities):
            answer += 1
            if location == 0:
                return answer
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
        
        if location == 0:
            location = len(priorities) - 1
        else:
            location -= 1
    return answer