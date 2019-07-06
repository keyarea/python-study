# 字典

在Python中， 字典是一系列键—值对。每个键都与一个值相关联，你可以使用键来访问与之
相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对
象用作字典中的值。

## 定义一个字典

```python
# 定义一个字典
person = {'name': "kai", 'age': 26}
```

##  访问字典中的值

```python
person = {'name': "kai", 'age': 26}
# 根据键获取字典的值
print(person['name'])  # kai
```

## 添加键值对

```python
person = {'name': 'kai', 'age': 26}
# 添加键值对
person['height'] = 180
print(person)  # # {'name': 'kai', 'age': 26, 'height': 180}
```

## 删除键值对

```python
person = {'name': 'kai', 'age': 26, 'height': 180}
# 删除键值对
del person['height']

print(person)  # {'name': 'kai', 'age': 26}
```

## 修改字典中的值

```python
person = {'name': 'kai', 'age': 26}
# 修改字典中的值
person['age'] = 25
print(person)  # {'name': 'kai', 'age': 25}
```

## 遍历字典

### 遍历键值对

```python
# 定义一个字典
person = {'name': "kai", 'age': 26}
# 遍历字典的键值队
for key, value in person.items():
    print(key, value)

"""
name kai
age 26
"""
```

### 遍历键

```python
# 定义一个字典
person = {'name': "kai", 'age': 26}
# 遍历字典的健
for key in person.keys():
    print(key)

"""
name
age
"""
```

### 遍历值

```python
# 定义一个字典
person = {'name': "kai", 'age': 26}
# 遍历字典的值
for value in person.values():
    print(value)

"""
kai
26
"""
```