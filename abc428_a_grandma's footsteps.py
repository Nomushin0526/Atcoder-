#Problem AtCoder ABC428 A
#Logic: Calculate the total distance/
#Total Distance = (Cycles * A) + (Remaning time)

S,A,B,X = map(int,input().split())

C=X//(A+B)
D=X%(A+B)


if A>X:
  print(S*X)
elif A==X:
  print(S*A)
else:
  if D>=A:
    print(S*A*C + A*S)
  else:
    print(S*A*C + D*S)
