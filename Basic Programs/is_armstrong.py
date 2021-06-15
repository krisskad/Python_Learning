# Given number is armstrong or not

"""
N = 100
1**3 + 0**3 + 0**3 = 1

100 is not armstrong

N = 153
1**3 + 5**3 + 3**3 = 1 + 125 + 9 = 153

"""


def isarm(order, N):
    calc = list(N)
    ans = 0

    for i in calc:
        ans = ans + pow(int(i), order)

    if int(N) == ans:
        return True
    else:
        return False


N = input("Enter Number: ")

order = len(N)
ans = isarm(order, N)
print(ans)