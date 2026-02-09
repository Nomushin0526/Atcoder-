#Problem: AtCoder ABC430 A
#Logic: Coding only Condition for outputting 'Yes' 
#Condition: C>=A and D<B

A, B, C, D = map(int, input().split())

if C>=A and D<B:
  print('Yes')
else:
  print('No')
