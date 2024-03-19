def solution(arr):
    #배열 오름차순 정렬 후 다른 배열에 저장
    #새로 만든 배열의 맨 앞 요소 값
    #for arr.length에서 if arr[i] == 최소값이면 del arr[i]
    #return 
    #if arr 요소 한 개면 replace -1하고 return
    #replace는 문자열이었다ㅠ
    
    if len(arr) == 1:
        arr[0] = -1
        return arr
    arr.remove(min(arr))
    
    return arr