def containsNumber(str):
    num_list = []
    for c in str:
        if c.isdigit():
            num_list.append(int(c))
    return num_list


def sum_avg_nums(str):
    num_list = containsNumber(str)
    numsum = sum(num_list)
    print("The sum of the numbers in the string ", (sum(num_list)))
    print("The average of the numbers in the string",
          (sum(num_list)/len(num_list)))


print("Enter the string")
str = str(input())
sum_avg_nums(" 1 shel 2")
