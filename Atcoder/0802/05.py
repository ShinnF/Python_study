from collections import deque

def bfs_lex_min_path(N, adj, start, goal):
    visited = [False] * (N + 1)
    parent = [-1] * (N + 1)
    
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)
                if v == goal:
                    break

    # パスの復元
    path = []
    cur = goal
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path
