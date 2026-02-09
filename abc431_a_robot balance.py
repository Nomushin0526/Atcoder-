#Problem: AtCoder ABC431 A
#Logic: Output the difference between H and B only when the head H is heavier than the torso B.

H, B = map(int,input().split())

c = H - B

if H>B:
  print(c)
else:
  print('0')
