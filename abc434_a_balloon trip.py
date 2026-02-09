#Probelm: AtCoder ABC434 A
#Logic: Divide W by B find n
#mathmatical formula: n = W//B + 1

W, B = map(int, input().split())

n = W * 1000 // B + 1
print(n)
