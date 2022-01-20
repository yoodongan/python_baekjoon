# 101 > 201 > 301 > ... H01   //  102 > 202 > 302 > ... H02  // ...
# 가로로 총 W개 만큼, 세로로 H개 만큼 있다. 한 텀 당 H개 씩.  H.H.H.H.  (W개)
T = int(input())
for i in range(T):
    h, w, n  = map(int, input().split())
    room_num = n // h + 1
    floor =  n % h 
    if floor == 0 :
        floor = h
        room_num-=1
    print(floor *100 + room_num)