# print fibonacci sequence till given number
# 0, 1, 1, 2, 3, 5, 8, 13,

N = int(input())


feb = [0,1]
for i in range(1, N+1):
    temp = feb[i-1] + feb[i]
    if temp>N:
        break
    feb.append(temp)

print(feb)