# Approach:
# 1. Count the number of fresh oranges and add all rotten oranges' positions to the queue.
# 2. Perform BFS from all initially rotten oranges, spreading rot to adjacent fresh oranges level by level (minute by minute).
# 3. If after BFS, there are no fresh oranges left, return the time taken. Otherwise, return -1.

# Time Complexity: O(N * M) — where N is the number of rows and M is the number of columns (each cell is processed once)
# Space Complexity: O(N * M) — for storing the queue in the worst case (all oranges are rotten)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]  # right, left, down, up
        q = deque()

        # Count fresh oranges and enqueue rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # BFS traversal to rot adjacent fresh oranges
        while q and fresh:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Skip out of bounds or non-fresh oranges
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2  # Rot the orange
                    q.append((nr, nc))
                    fresh -= 1  # Decrease fresh orange count
            time += 1  # Increase time for each level (minute)

        return time if fresh == 0 else -1  # If all fresh oranges rotted, return time else -1
