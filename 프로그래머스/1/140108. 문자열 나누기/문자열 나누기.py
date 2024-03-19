def solution(s):
    answer = 0
    x_cnt = 0
    others_cnt = 0
    for i in s:
        if x_cnt == others_cnt:
            answer += 1
            val = i
        if val == i: 
            x_cnt += 1
        else:
            others_cnt += 1
    return answer