def isPal(n):
    for i in range(len(n) // 2):
        if (n[i] != n[-1 - i]):
            return False

    return True


def convertNumIntoString(num):
    n = str(num)
    return n

def closestPalindrome(num):

    snum = num - 1
    while (not isPal(
            convertNumIntoString(abs(snum)))):
        snum -= 1


    lnum = num + 1
    while not isPal(
           convertNumIntoString(lnum)):
        SPNum += 1

    # Check absolute difference
    if abs(num - snum) > abs(num - lnum):
        return lnum
    else:
        return snum


if __name__ == '__main__':
    num = 121

    print(closestPalindrome(num))