#Day 28.
#1631. Path With Minimum Effort

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        ret = [[math.inf for _ in range(n)] for _ in range(m)]
        ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        nodes = [(0, 0, 0)]
        while nodes:
            cost, x, y = heapq.heappop(nodes)
            if cost >= ret[x][y]:
                continue
            ret[x][y] = cost
            for dx, dy in ds:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    ncost = max(cost, abs(heights[x][y] - heights[nx][ny]))
                    if ncost < ret[nx][ny]:
                        heapq.heappush(nodes, (ncost, nx, ny))
        return ret[-1][-1]
