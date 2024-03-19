import re
def solution(my_string):
    answer = []
    #문자열에서 숫자(인 문자)열 추출
    string = re.sub(r'[^0-9]', '', my_string)
    answer = list(map(int, str(string)))
    #오름차순 정렬
    answer.sort()   
    return answer