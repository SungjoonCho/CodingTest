# 2xn 타일링 - 백준 

n = int(input())-1

cnt = [1,2]

if(n>=2):    
    for i in range(2,n+1):
        cnt.append(cnt[i-2] + cnt[i-1])
    
print(cnt[n]%10007)
