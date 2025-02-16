def solution(n, lost, reserve):
    answer = n
    lost_student = [0] * 31
    
    lost = set(lost)
    reserve = set(reserve)
    
    for i in lost - reserve:
        lost_student[i] = 1
        answer -= 1
    
    for i in reserve - lost:
        for j in [i - 1, i + 1]:
            if lost_student[j] == 1:
                lost_student[j] = 0
                answer += 1
                break
    return answer
