# 피보나치를 배열로 만들어서 풀어보기.
n=int(input())
s=[0,1]
for i in range(2, n+1):
    s.append(s[i-1] + s[i-2])
print(s[n])