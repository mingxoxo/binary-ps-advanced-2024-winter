def dfs(numbers, target, res = 0, idx = 0):
    if idx == len(numbers):
        return int(res == target)
    
    return (dfs(numbers, target, res + numbers[idx], idx + 1) + 
            dfs(numbers, target, res - numbers[idx], idx + 1))

    
def solution(numbers, target):
    return dfs(numbers, target)
