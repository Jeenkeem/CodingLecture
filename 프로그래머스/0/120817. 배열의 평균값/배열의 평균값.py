def solution(numbers):
    if len(numbers) == 0:
        return 0
    answer = 0
    for i in numbers:
        answer += i

    return answer/len(numbers)