def solution(triangle):
    dp = [[0] * (i + 1) for i in range(len(triangle[-1]))]
    
    dp[0][0] = triangle[0][0]
    for i in range(len(triangle) - 1):
        for j in range(i + 1):
            for k in range(j, j + 2):
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + triangle[i + 1][k])
            
    answer = max(dp[-1])
    return answer
