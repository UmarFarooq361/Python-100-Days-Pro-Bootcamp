# number = [5,2,3]
# new_list = [n+1 for n in number]
# print(new_list)

# rangel_list = [n*2 for n in range(1,5)]
# print(range_list)


# day 26.1 challenge for squared the number in the list using list comprehension
# numbers = [1, 1, 4, 6, 7]
# squared_list = [n*n for n in numbers]
# print(squared_list)

# day 26.2 even number in the list comprehension
# numbers = [1, 1, 4, 6, 7]
# even_list = [num for num in numbers if num % 2 == 0]
# print(even_list)

# day 26.3 read and compare number from two files using list comprehension
# with open("file1.txt") as file1:
#     file1_num = file1.readlines()
# with open("file1.txt") as file2:
#     file2_num = file2.readlines()
# result = [int(num) for num in file1_num if num in file2_num]
# print(result)

# day 26.4 exercise of dictionary conprehension
sentence =  "what is your name handsome boy"
sentence_list = sentence.split(" ")
result = {word:len(word) for word in sentence_list}
print(result)
