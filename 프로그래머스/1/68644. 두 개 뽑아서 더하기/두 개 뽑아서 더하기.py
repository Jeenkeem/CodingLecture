def solution(numbers):
    #빈 배열 먼저 
    lst = []
    
    #두 수 합 모두 구해서 바로 빈 배열에 넣기
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            lst.append(numbers[i] + numbers[j])
    
    #중복 제거 + 정렬
    lst = sorted(set(lst))
    
    return lst