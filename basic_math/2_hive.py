N = int(input())
cnt = 1
pile_count = 1
while N > pile_count:
    pile_count += 6*cnt
    cnt+=1
print(cnt)