import sys
sys.setrecursionlimit(20000000)
N, M = map(int, input().split())
# edgeを作る。
max_flow = 0
Edge_list = [[] for i in range(N)]
Y = [0]
flag = 0
for i in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    Edge_list[u] += [[v, c, len(Edge_list[v])]]
    Edge_list[v] += [[u, 0, len(Edge_list[u])-1]]


def dfs_ff(s, e, flow):
    if (s == e):
        return flow
    visited[s] = True  # その開始ノードは訪れたということ。
    for node in Edge_list[s]:  # iは要素
        if node[1] > 0 and visited[node[0]] == 0:
            f = dfs_ff(node[0], e, min(flow, node[1]))
            if f > 0:
              
                node[1] -= f  
                Edge_list[node[0]][node[2]][1] += f
                return f
               
    return 0


while True:
    visited = [False for _ in range(N)]
    f = dfs_ff(0, N-1, 10**9)
    if not f:
        break
    max_flow += f
print(max_flow)
