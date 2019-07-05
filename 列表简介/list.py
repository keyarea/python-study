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

cars.append("丰田")
print(cars)  # ['路虎', '奔驰', '凯迪拉克', '大众', '丰田']
cars.insert(2, "本田")
print(cars)  # ['路虎', '奔驰', '本田', '凯迪拉克', '大众', '丰田']
