'''
# formula
# A = P(1+R/100)^t
# compound interest = A -P

Where,
A is amount
P is principle amount
R is the rate and
T is the time span
'''


def com_int(P, R, T):
    A = P * (pow((1 + R / 100), T))
    CI = A - P
    return CI


P = int(input("Principle Amt: "))
R = int(input("Rate of Interest: "))
T = int(input("Years: "))

print("{:.2f}".format(com_int(P, R, T)))
