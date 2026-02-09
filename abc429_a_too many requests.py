#Problem: AtCoder ABC429 A
#Logic: Decide range 
#Range: 1 < i < N + 1

N, M = map(int, input().split())

for i in range(1, N + 1):
  if i <= M:
    print('OK')
  else:
    print('Too Many Requests')
