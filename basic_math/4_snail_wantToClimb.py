import math
A, B, V = map(int, input().split())

# n(소요시간) * (A-B) + A = V. 마지막 날 A만큼 올라가야 도착하므로 그 날 (1일치)는 제외되어 있다. 따라서 n(소요시간) = (V-A)/(A-B)+1
duration = math.ceil((V-A)/(A-B))+1
print(duration)