import numpy as np

def dtw(s1, s2):
    m, n = len(s1), len(s2)
    dp = np.full((m+1, n+1), np.inf)
    dp[0, 0] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            cost = abs(s1[i-1] - s2[j-1])
            dp[i, j] = cost + min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1])

    path = backtrack(dp)
    return dp[m, n], path

def backtrack(cost_matrix):
    i, j = cost_matrix.shape[0] - 1, cost_matrix.shape[1] - 1
    path = [(i-1, j-1)]

    while i > 1 or j > 1:
        if i == 1:
            j -= 1
        elif j == 1:
            i -= 1
        else:
            min_cost = min(cost_matrix[i-1, j], cost_matrix[i, j-1], cost_matrix[i-1, j-1])
            if cost_matrix[i-1, j-1] == min_cost:
                i, j = i-1, j-1
            elif cost_matrix[i-1, j] == min_cost:
                i -= 1
            else:
                j -= 1
        path.append((i-1, j-1))

    return path[::-1]