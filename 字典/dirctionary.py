# 定义一个字典
person = {'name': "kai", 'age': 26}

# 根据键获取字典的值
print(person['name'])  # kai

# 遍历字典的键值队
for key, value in person.items():
    print(key, value)

"""
name kai
age 26
"""

# 遍历字典的健
for key in person.keys():
    print(key)

"""
name
age
"""

# 遍历字典的值
for value in person.values():
    print(value)

"""
kai
26
"""

# 添加键值对
person['height'] = 180
print(person)  # {'name': 'kai', 'age': 26, 'height': 180}

# 删除键值对
del person['height']

print(person)  # {'name': 'kai', 'age': 26}


# 修改字典元素
person['age'] = 25

print(person)  # {'name': 'kai', 'age': 25}

