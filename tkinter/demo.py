# def power_of_n(a, n):
#     b = []
#     for i in a:
#         b.append(i ** n)
#     return b
#
#
# #
# def function1(numbers, power):
#     numbers_list = map(int, numbers.split())
#     total = power_of_n(numbers_list, int(power))
#     avg = sum(total) / len(total)
#     return f'total sum of numbers = {total} \n average of sum of power{power} of numbers = {sum(total)}/{len(total)} = {round(avg, 4)}'
#     # return sum(numbers_list)


# a=[1,3,4,5]
# b=4
# function1(a,b)

def nameit(name):
    greetings = f'hello {name}'
    return greetings
