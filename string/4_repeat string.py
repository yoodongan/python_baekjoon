T = int(input())
for i in range(T):
    r, s = input().split() 
    for i in s:
        print(i * int(r), end='')
    print()
