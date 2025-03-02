from collections import deque

def bfs(computers, n, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        x = queue.popleft()
        for idx in range(n):
            if computers[x][idx] == 0 or visited[idx] is True:
                continue
            visited[idx] = True
            queue.append(idx)
            

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i] is True:
            continue
        answer += 1
        bfs(computers, n, i, visited)
    return answer
