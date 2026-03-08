import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g = {start: 0}

    while open_list:

        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:

            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:

                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                new_cost = g[current] + 1

                if neighbor not in g or new_cost < g[neighbor]:

                    g[neighbor] = new_cost
                    f = new_cost + heuristic(neighbor, goal)

                    heapq.heappush(open_list, (f, neighbor))
                    came_from[neighbor] = current

    return None


maze = [
[0,1,0,0,0],
[0,1,0,1,0],
[0,0,0,1,0],
[1,1,0,0,0],
[0,0,0,1,0]
]

start = (0,0)
goal = (4,4)

path = astar(maze, start, goal)

print("Path through the maze:")
print(path)