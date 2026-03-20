@memoize
def grid_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return grid_paths(m - 1, n) + grid_paths(m, n - 1)

print("Путей в сетке 3x3:", grid_paths(3, 3))
