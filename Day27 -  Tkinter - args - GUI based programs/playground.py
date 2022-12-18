# def add(*Args):
#     sum = 0
#     for n in Args:
#         sum += n
#     # total =  sum(Args)
#     return sum
#
# total_sum = add(2,3 ,5 )
# print(total_sum)

def calculator(**kwargs):
    print(kwargs)
    n = 0
    for (key, value) in kwargs.items():
        print(key)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

print(calculator(add=3, multiply= 5))