def solution(n):
    f = [0, 1]
    
    for i in range(2,n+1,1):
        f.append(f[i-1] + f[i-2])
    
    return f[-1]%1234567