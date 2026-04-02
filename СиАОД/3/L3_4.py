def min_path_cost(grid):
    n, m = len(grid), len(grid[0])
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = grid[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    path = []
    i, j = n-1, m-1
    while i > 0 or j > 0:
        path.append((i, j))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i-1][j] < dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    path.append((0, 0))
    path.reverse()

    return dp[n-1][m-1], path

grid = [[((i * 13 + j * 19 + 5) % 7) + 1 for j in range(128)] for i in range(128)]
for i in range(40, 90):
    for j in range(50, 55):
        grid[i][j] = 20
for i in range(70, 100):
    for j in range(80, 120):
        grid[i][j] = 15

min_cost, route = min_path_cost(grid)
print(f"Минимальная стоимость: {min_cost}")
print(f"Маршрут (первые 10 шагов): {route[:10]}")
