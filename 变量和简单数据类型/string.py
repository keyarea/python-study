#!/usr/bin/env python3

# 定义了一个字符串
message = "hello world"

# 将每个单词的首字符变为大写
print(message.title())  # Hello World

# 字符串全部变为大写
print(message.upper())  # HELLO WORLD

# 字符串全部小写
print(message.lower())  # hello world

# 拼接字符串
first_name = "kai"
last_name = "wang"
full_name = first_name + " " + last_name
print(full_name)  # kai wang

# 添加空白
print("\thello world")
print("hello \nworld")

# 删除空白
two_sides_blank = "  hello  "

del_left_blank = two_sides_blank.lstrip()  # 删除左侧空白
del_right_blank = two_sides_blank.rstrip()  # 删除右侧空白
del_blank = two_sides_blank.strip()  # 删除两侧空白

print(del_left_blank)
print(del_right_blank)
print(del_blank)
