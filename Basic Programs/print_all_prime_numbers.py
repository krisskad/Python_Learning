# prime number can only divisible by 1 and by itself

def all_prime(start, end):
    for i in range(start, end +1):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i, end=" ")


start, end = (int(x) for x in input().split())

all_prime(start, end)
