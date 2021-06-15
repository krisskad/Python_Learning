# factorial

# N = 5
# 5*4*3*2

# loop
# fact = 1
# for x in range(2,int(input())+1):
#     if x==0:
#         fact = 1
#         break
#     else:
#         fact = fact * x
# print(fact)


# recursion
def fact(N):
    if N == 0:
        return 1
    else:
        return N*fact(N-1)

print(fact(100))

# formula

