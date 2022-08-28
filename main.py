

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# f = open('example.txt', 'r')
# # ab = open('C:/xyz.txt', 'r')
# try:
#     print(*f)
# finally:
#     f.close()


# with open ('example.txt') as f:
#     print(*f)

# f = open('example.txt', 'r')
# print(f.read(7))
# print(f.read(7))
# print(f.read())
# f.close

# x = open('text.txt', 'r')
# print(x.readline())
# print(x.readline())
# print(x.readline())
# x.close

# x = open('text.txt', 'r')
# print(x.readlines())
# x.close

# f = open('xyz.txt', 'w')
# f.write('Hello \nWorld')
# f.close()
# f = open('xyz.txt', 'r')
# print(f.read())
# f.close

import os
# os.rename("xyz.txt", "abc.txt")

# print("Текущая деректория:", os.getcwd())
# os.mkdir("folder")

# os.chdir("folder")
# print("Текущая директория изменилась на folder:", os.getcwd())
# os.chdir("..")
# os.makedirs("nested1/nested2/nested3")
# print(os.getcwd())

# os.remove("abc.txt")
# os.rmdir("folder")

# os.removedirs("nested1/nested2/nested3")

# with open('task1.txt') as f:
#     s = f.readlines()
# for i in s:
#     i = i.replace('_', ' ')
#     l = i.split(' ')
# print(l)
# sum = 0
# for i in l:
#     if i.isdigit():
#         i = int(i)
#         sum += i
# print(sum)

# a = open('task2.txt')
# b = []
# c = []
# s = a.readlines()
# print(s)
# for i in s:
#     i = i[:-1]
#     if i.isalpha():
#         i = str(i)
#         b.append(i)
#     elif i.isdigit():
#         i = int(i)
#         c.append(i)
# print(b)
# print(c)
# c.sort()
# b.sort()
# mas = c + b
# print(mas)

# fname = input('Файл: ')
# f = open(fname, 'w')
# while True:
#     s = input()
#     if s == '':
#         break
#     f.write(s + '\n')
# f.close()

# f = open('task4.txt')
# line = 0
# for i in f:
#     line += 1
#     print(i, len(i), 'симв.')
# print(line, 'стр.')
# f.close







