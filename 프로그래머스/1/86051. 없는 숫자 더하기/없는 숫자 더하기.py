def solution(numbers):
    answer = 0
    #for문으로 순서대로 0~9배열에서 빼기
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer