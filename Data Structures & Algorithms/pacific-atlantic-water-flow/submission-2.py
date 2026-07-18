class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacifique = set()
        atlantique = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                    dfs(nr, nc, visited)

        for c in range(COLS):
            dfs(0, c, pacifique)
            dfs(ROWS - 1, c, atlantique)

        for r in range(ROWS):
            dfs(r, 0, pacifique)
            dfs(r, COLS - 1, atlantique)

        return list(pacifique.intersection(atlantique))
        