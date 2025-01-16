def solution(arr1, arr2):
    # arr1 행, 열 크기 
    r1, c1 = len(arr1), len(arr1[0])
    # arr2 행, 열 크기
    r2, c2 = len(arr2), len(arr2[0])
    
    # 결과값 용 빈 2차원 배열 선언
    result = [[0] * c2 for _ in range(r1)]
    
    # for문 중첩으로 행렬 곱 더해서 결과 값에 넣어주기
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result
    
    
    
    