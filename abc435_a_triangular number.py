#Problem: AtCoder ABC435 A
#Logic: Set the range and keep incrementing i

N = int(input())

c = 0
for i in range(1, N + 1):
  c += i
  
print(c)
