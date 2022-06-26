# number =1
# while number < 11:
#     if number ==5:
#         continue
#     print(number)
#     number += 1
# else:
#     print("All went well")
import random

# n = 1231
# n = str(n)
# print(n == n[::-1])
# a = 12321
# a = str(a)
# print(a == a[::-1])
#
# b = "Hello world"
# print(len(b))
# print(b * 3)
#
# chr = 'spam' + '_' + 'spam-'
# print(chr)
# for i in range(1, 11,):
#     print('i'*i)
#
# for j in range(11, 0, -1):
#     print('j'* j)
#
# for a in range(1, 11):
#     for b in range(11, 1):
#             print('a'*a)
#
# a_str = 'spam'
# new_str = a_str[:1] + 'l' + a_str[2:]
# print(new_str)

# for character in 'Programming':
#     print(character, end=' ')
#
# digit = 10, 20, 30, 40
#
# print(digit, sep='')
#
# for number in range(1, 15):
#     print(number, end=' ')
#
# total = 0
# for grades in [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]:
#     total = total + grades
# average = int(total / 10)
#
# print('the total score of ten students is ', total, ' and the average score is ', average)

# # initialization phase
# counter = 0
# sum_total = 0
#
# # processing phase
# while counter < 10:
#     grade = int(input("enter a student grade: "))
#     sum_total += grade
#     counter += 1
# # termination phase
# average = float(total/counter)
# print(f"the total of {counter} student is {total} and the average score is {average}")
#
# count = 0
# total_score = 0
#
# grade_score = int(input('enter student grade, -1 to end: '))
# while grade_score != -1:
#     total_score += grade_score
#     count += 1
#     grade_score = int(input('enter student grade, -1 to end: '))
#
# average_score = float(total_score/count)
# print("the total score of", count, "student is", total_score, "and the average is", average_score)


# def rotate(lst, k):
#     k = k % len(lst)
#     return lst[-k:] + lst[:-k]
#
# print(rotate([1,2,3,4,5], 18))
#
#
# # how to build a list
# lst = []
# for i in range(1, 11):
#     lst.append(i)
#
# # or
# list(range(1, 11))
#
# # list comprehension
# [i for i in range(1, 11)]
#
# [i for i in range(1, 11) if i % 2 == 0]

lst = [num for num in range(1, 11)]
evens = [num for num in range(1, 11) if num % 2 == 0]
even_and_Squared_odds = [num if num % 2 == 0 else num**2 for num in range(1, 11)]

digit = int(input("enter a digit: "))

lst_input = [int(input('enter a number: ')) for num in range(digit)]


print(lst)
print(evens)
print(even_and_Squared_odds)
print(lst_input)

print(even_and_Squared_odds)
# print(list_input)
list_nested_for = [(x, y) for x in range(1, 5) for y in range(6, 10)]
print(list_nested_for)
upper_names = [name for name in ["dolapo", "tolani", "florence"]]
print(upper_names)


list_of_dicts = [{key: value} for key, value in zip(upper_names, evens)]
print(list_of_dicts)




