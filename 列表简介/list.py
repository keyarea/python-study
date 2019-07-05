#!/usr/bin/env python3

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers)  #  [1, 2, 3, 4, 5, 6, 7, 8]

books = ["javascript高级程序设计", "第一行代码", "python基础"]
print(books[2])  # python基础
print(books[-1]) # python基础
#print(books[3])  # IndexError: list index out of range

cars = ["玛莎拉蒂", "奔驰", "凯迪拉克", "大众"]
print(cars)  # ["玛莎拉蒂", "奔驰", "凯迪拉克", "大众"]
cars[0] = "路虎"
print(cars)  # ['路虎', '奔驰', '凯迪拉克', '大众']

phones = ["三星", "苹果"]
phones.append("小米")
print(phones) # ['三星', '苹果', '小米']

phones.insert(1, "华为")
print(phones)  # ['三星', '华为', '苹果', '小米']

del phones[0]
print(phones)  # ['华为', '苹果', '小米']

phone = phones.pop()  # 删除列表中的最后一个元素并返回该值
print("为发烧而生的手机: " + phone)  # 为发烧而生的手机: 小米
print(phones)  #  ['华为', '苹果']

apple = phones.pop(1)  # 删除列表中的索引的值，并将其返回
print("堪称奢侈品的手机：" + apple)  #  堪称奢侈品的手机：苹果
print(phones) # ['华为']


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']


letters = ["p", "b", "i", "n", "m"]
letters.sort()
print(letters)  # ['b', 'i', 'm', 'n', 'p']

letters = ["p", "b", "i", "n", "m"]
letters.sort(reverse = True)
print(letters)  # ['p', 'n', 'm', 'i', 'b']

letters = ["p", "b", "i", "n", "m"]
print(sorted(letters)) # ['b', 'i', 'm', 'n', 'p']
print(letters)  # ['p', 'b', 'i', 'n', 'm']

letters = ["p", "b", "i", "n", "m"]
print(sorted(letters, reverse = True))  # ['p', 'n', 'm', 'i', 'b']
print(letters)  # ['p', 'b', 'i', 'n', 'm']

letters = ["p", "b", "i", "n", "m"]
letters.reverse()
print(letters) # ['m', 'n', 'i', 'b', 'p']

letters = ["p", "b", "i", "n", "m"]
print(len(letters)) # 5



letters = ["p", "b", "i", "n", "m"]
for letter in letters:
    print(letter)
    print("有请下一个字母")
print("字母遍历完毕")

'''
p
有请下一个字母
b
有请下一个字母
i
有请下一个字母
n
有请下一个字母
m
有请下一个字母
字母遍历完毕
'''

for value in range(1, 10):
    print(value)

"""
1
2
3
4
5
6
7
8
9
"""

numbers = list(range(1, 10))
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]


numbers = list(range(2, 11, 2))
print(max(numbers))  # 10
print(min(numbers))  # 2
print(sum(numbers))  # 30

numbers = [value ** 2 for value in range(1, 11)]
print(numbers) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[1:3]) # [2. 3]
print(numbers[:3]) # [1, 2, 3]
print(numbers[:]) # [1, 2, 3, 4, 5, 6, 7]
print(numbers[2:]) # [3, 4, 5, 6, 7]
print(numbers[-3:]) # [5, 6, 7]

a = [1, 2, 3, 4, 5, [6, 7, 8]]
b = a[:]
a[-1].append(9)
print(a)  # [1, 2, 3, 4, 5, [6, 7, 8, 9]]
print(b)  # [1, 2, 3, 4, 5, [6, 7, 8, 9]]