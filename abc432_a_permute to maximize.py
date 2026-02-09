#Problem: AtCoder ABC432 A
#Logic: Sort A, B and C in ascending order

A, B, C = map(int,input().split())

L = sorted([A, B, C], reverse=True)
print(str(L[0]) + str(L[1]) + str(L[2]))
