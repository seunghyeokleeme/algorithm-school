class UnionFind:
    def __init__(self, n):
        # 모든 정점들이 각각의 집합에 속하도록 초기화합니다.
        self.parent = [i for i in range(n)]
    
    def find(self, u):
        # 재귀를 통해 u가 속한 집합의 대표(루트)를 찾습니다.
        if u == self.parent[u]:
            return u
        # 경로 압축: u의 부모를 u의 루트로 바로 연결합니다.
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        # u와 v의 루트를 찾아서 합칩니다. (u의 루트가 v의 루트를 가리키도록 합니다.)
        root1 = self.find(u)
        root2 = self.find(v)
        self.parent[root2] = root1

def kruskal(graph):
    # 정점의 개수를 계산합니다.
    vertices = max(max(u, v) for u, v, _ in graph) + 1
    
    # Union-Find 인스턴스를 생성합니다.
    uf = UnionFind(vertices)
    # 최소 신장 트리를 저장할 리스트를 초기화합니다.
    mst = []

    # 간선들을 가중치 기준으로 정렬합니다.
    graph.sort(key=lambda edge: edge[2])

    # 정렬된 간선들을 순회합니다.
    for edge in graph:
        u, v, _ = edge
        # u와 v가 다른 집합에 속해 있다면,
        if uf.find(u) != uf.find(v):
            # 두 집합을 합치고,
            uf.union(u, v)
            # 현재의 간선을 최소 신장 트리에 추가합니다.
            mst.append(edge)
    
    # 완성된 최소 신장 트리를 반환합니다.
    return mst

# 그래프 정의
graph = [(1, 2, 1), (2, 5, 1), (1, 5, 2), (0, 3, 2), (3, 4, 3), (0, 4, 4), (1, 3, 4), (3, 5, 7), (0, 1, 8), (4, 5, 9)]  # 예시입니다. 실제 간선 정보를 넣어주세요.

# Kruskal 알고리즘 실행
mst = kruskal(graph)

# 출력
for edge in mst:
    print(edge)
