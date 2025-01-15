def solution(numbers):
    # 1. result 만들 빈 배열 만들기
    ret = []
    
    # 2. for문으로 numbers 순회하며 더하기
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            ret.append(numbers[i] + numbers[j])
    
    # 3. set()중복제거, sort()오름차순
    ret = sorted(set(ret))
    
    return ret
            