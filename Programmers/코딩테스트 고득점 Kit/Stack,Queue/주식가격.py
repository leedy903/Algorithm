'''
Solution 1
keyword: brute force
'''
def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        ans = len(prices) - i - 1
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                ans = j - i
                break
        answer.append(ans)
    answer.append(0)
    return answer


'''
Solution 2 - 다른 사람의 풀이 참고
keyword: stack
'''
# def solution(prices):
#     NUMBER_OF_PRICES = len(prices)
#     answer = [0 for _ in range(NUMBER_OF_PRICES)]
    
#     price_stack = []    # [[index, price]]
#     for i in range(NUMBER_OF_PRICES):
#         while price_stack != [] and price_stack[-1][1] > prices[i]:
#             index, _ = price_stack.pop()
#             answer[index] = i - index
#         price_stack.append([i, prices[i]])
    
#     for index, _ in price_stack:
#         answer[index] = NUMBER_OF_PRICES - index - 1
    
#     return answer