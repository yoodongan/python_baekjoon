t = int(input())
for i in range(t):
    k,n = map(int, input().split())

    first_floor = [i for i in range(1,n+1)]  # 1층 1호~n호 까지 배열로 채우기.
    for floor in range(k):
        for room in range(1, n):     # 배열 인덱스 기준으로, 1호는 0번째 인덱스임.
            first_floor[room] += first_floor[room-1]
    print(first_floor[n-1])   # 반복문으로 k층까지는 도달, 방으로 가기 위해서는 n호로 가야함. n호는 인덱스 기준으로 n-1로 치환.

