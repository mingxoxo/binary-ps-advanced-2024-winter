def solution(N, number):
    dp = [set()] + [{int(str(N) * (i + 1))} for i in range(8)]

    for i in range(1, 9):
        for j in range(1, i // 2 + 1):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i] |= {num1 + num2, num1 - num2, num1 * num2, num2 - num1}
                    if num1 != 0:
                        dp[i].add(num2 // num1)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        if number in dp[i]:
            return i
    
    return -1
