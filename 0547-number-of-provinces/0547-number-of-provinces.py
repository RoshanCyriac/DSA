class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        seen = set()
        provinces = 0

        def dfs(city):
            seen.add(city)

            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and neighbour not in seen:
                    dfs(neighbour)

        for city in range(n):
            if city not in seen:
                provinces += 1
                dfs(city)

        return provinces