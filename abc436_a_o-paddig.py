#Problem: AtCoder ABC436 A
#Logic: minus N by S'length

N = int(input())
S = input()

X = N - int(len(S))
print('o' * X + S)
