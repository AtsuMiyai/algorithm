INF = 10***9
pre_choten = [None]*2000000
pre_hen = [None]*2000000


def min_cost_flow(start, end, flow):
    res = 0
    while (1):
        if (flow <= 0):
            break
        dist = [INF]*(20000)
        dist[start] = 0
        flag = 1  # 更新されているなら1、されなかったら0とする。
        while (flag):
            flag = 0
            for i in range(V):
                if (dist[i] == INF):
                    continue
                j = 0
                for edge in edge_list[i]:
                    if (edge[2] > 0 and dist[edge[0]] > dist[i]+edge[1]):
                        dist[edge[0]] = dist[i]+edge[1]
                        pre_choten[edge[0]] = i
                        pre_hen[edge[0]] = j
                        flag = 1
                    j += 1
        if (dist[end] == INF):
            return -1
        min1 = flow
        v = end
        while (v != start):
            node = edge_list[pre_choten[v]][pre_hen[v]]

            min1 = min(min1, node[2])
            v = pre_choten[v]
        flow -= min1
        res += min1*dist[end]
        v = end
        while (v != start):
            node = edge_list[pre_choten[v]][pre_hen[v]]
            node[2] -= min1

            edge_list[v][node[3]][2] += min1
            v = pre_choten[v]
    return res


print(min_cost_flow(0, V-1, len(T)))
