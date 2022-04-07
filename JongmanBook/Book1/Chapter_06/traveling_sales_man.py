

def shortestPath(path: list, visited: list, currentLength: int):
    # base case
    if len(path == n):
        return currentLength + dist[path[0]][path[-1]]
    ret = INF
    # try all rest city
    for next_city in range(n):
        if visited[next_city]:
            continue
        here = path[-1]
        path.append(next_city)
        visited[next_city] = True
        # take shortest path length by completing the rest of the path using recursion call
        cand = shortestPath(path, visited, currentLength + dist[here][next_city])
        ret = min(ret, cand)
        visited[next_city] = False
        path.pop()

    return ret



INF = 987654321
MAX = 987654321
dist = [[0 for _ in range(MAX)]for _ in range(MAX)]

n = int(input())

