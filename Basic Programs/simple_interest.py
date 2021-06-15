# formula
# simple interest = amt*percentage*time/100

P, R, T = (int(x) for x in input().split())

ans = P*R*T/100
print(ans)