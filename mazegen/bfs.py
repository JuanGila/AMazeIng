from collections import deque


def bfs(s, t, adj):
    q = deque([s])
    seen = {s}
    while q:
        v = q.popleft()
        if v == t:
            return True
        for w in adj[v]:
            if w not in seen:
                q.append(w)
                seen.add(w)
    return False


def bfs_solver(s, goal, nbrs):
    q = deque([s])
    seen = {s}
    while q:
        u = q.popleft()
        if u == goal:
            return u
        for v in nbrs(u):
            if v not in seen:
                seen.add(v)
                q.append(v)