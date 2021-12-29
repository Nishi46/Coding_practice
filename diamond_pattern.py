def pypyramid(n):
    for i in range(0, n):
        for j in range(0, i=1):
            print("* ")
        print("\r")


print("How many lines would you like? ")
n = input()
pypyramid(n)
