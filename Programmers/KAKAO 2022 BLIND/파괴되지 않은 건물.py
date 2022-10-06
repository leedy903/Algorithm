def solution(board, skill):
    
    def show_map(_map: list, content:str = "prefix sum") -> None:
        print(content)
        max_num = max(map(max, _map)) 
        for r in range(len(_map)):
            for c in range(len(_map[0])):
                ps = _map[r][c]
                space = len(str(max_num)) - len(str(ps)) + 1
                print(" " * space, ps, end="")
            print()
        print()
        return
    
    answer = 0
    
    prefix_sum = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    
    for (_type, r1, c1, r2, c2, degree) in skill:
        sign = -1 if _type == 1 else 1
            
        prefix_sum[r1][c1] += sign * degree
        prefix_sum[r2 + 1][c1] -= sign * degree
        prefix_sum[r1][c2 + 1] -= sign * degree
        prefix_sum[r2 + 1][c2 + 1] += sign * degree
    
    show_map(prefix_sum, "get score")
    
    for c in range(len(prefix_sum[0])):
        for r in range(1, len(prefix_sum)):
            prefix_sum[r][c] += prefix_sum[r - 1][c]
    
    show_map(prefix_sum, "from top to bottom")
    
    for r in range(len(prefix_sum)):
        for c in range(1, len(prefix_sum[0])):
            prefix_sum[r][c] += prefix_sum[r][c - 1]
            
    show_map(prefix_sum, "from left to right")
        
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += prefix_sum[r][c]
            
    show_map(prefix_sum)
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] > 0:
                answer += 1
                
    return answer