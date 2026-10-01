class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        1. initialize a queue with positions of all rotten oranges
        2. count total number of fresh oranges
        3. while the queue is not empty and fresh oranges exist:
            - process all  nodes inside the queue
            - for each rotten orange:
                check all 4 neighbors
                if a neighbor is fresh
                    make it rotten
                    decrease fresh count
                    add it into the queue
            increment time by 1
        4. if fresh count becomes 0, return time
        5. otherwise, return -1
        '''
        q = collections.deque()
        time = 0
        fresh_oranges = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_oranges+=1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while fresh_oranges > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col  = r+dr, c+dc
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh_oranges-=1
            time+=1
        return time if fresh_oranges == 0 else -1