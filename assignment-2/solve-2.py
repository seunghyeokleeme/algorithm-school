import heapq
from collections import defaultdict

def prim_mst(edges):
    # 그래프의 인접 리스트 표현을 생성합니다.
    graph = defaultdict(list)
    
    for src, dest, cost in edges:
        graph[src].append((cost, dest))
        graph[dest].append((cost, src))
    
    # 우선순위 큐, 거리 배열 및 부모 딕셔너리를 초기화 합니다.
    p = 0
    D = {vertex: float('infinity') for vertex in graph}
    D[p] = 0
    
    T = {}
    # -1은 시작점이 없음을 의미합니다.
    parent = {vertex: (-1, float('infinity')) for vertex in graph}
    Q = []
    for vertex in graph:
        if vertex == p:
            heapq.heappush(Q, (0, vertex))
        else:
            heapq.heappush(Q, (float('infinity'), vertex))
    
    while Q:
        # 우선순위 큐에서 가장 거리가 짧은 정점을 꺼냅니다. 이 정점은 MST에 다음으로 포함될 정점입니다.
        _, vmin = heapq.heappop(Q)
        # 이 정점이 이미 T에 포함되어 있으면 이 정점을 스킵합니다.
        if vmin in T: 
            continue
        # vim을 MST에 포함시키고, 그 거리를 T에 저장합니다.
        T[vmin] = D[vmin]
        # vmin에 인접한 모든 정점에 대해 반복합니다.
        for cost, v_neighbor in graph[vmin]:
            # 만약 이웃하는 정점이 아직 MST에 포함되어 있지 않고 이 정점까지의 거리가 이전에 알려진 거리보다 작다면
            if v_neighbor not in T and cost < D[v_neighbor]:
                # 이웃하는 정점까지의 거리를 업데이트합니다.
                D[v_neighbor] = cost
                # 이웃하는 정점의 부모를 vim으로 설정하고 그 비용을 저장합니다.
                parent[v_neighbor] = (vmin, cost)
                # 우선순위 큐에 업데이트된 거리와 이웃하는 정점을 다시 푸시하여 해당 정점이 다음에 MST에 포함될 수 있게 합니다.
                heapq.heappush(Q, (cost, v_neighbor))
    
    # 부모 딕셔너리에서 MST 간선을 추출합니다.
    mst_edges = []
    for v, (u, w) in parent.items():
        if u != -1:
            mst_edges.append((u, v, w))
    return mst_edges

# 입력
edges = [
    (0, 1, 3),
    (0, 3, 2),
    (0, 4, 4),
    (1, 2, 1),
    (1, 3, 4),
    (1, 5, 2),
    (2, 5, 1),
    (3, 4, 5),
    (3, 5, 7),
    (4, 5, 9)
]

# 실행
mst = prim_mst(edges)

# 출력
for edge in mst:
    print(edge)
