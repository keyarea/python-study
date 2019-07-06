# while循环

## 使用while循环

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("while循环执行完毕！")

'''
1
2
3
4
5
while循环执行完毕！
'''
```


## 使用break结束循环

```python
message = "\n请输入你曾经去过的城市:"
message += "\n当你输入完毕，输入quit结束程序"

while True:
    city = input(message)

    if city == 'quit':
        break   # 退出该循环
    else:
        print("我喜欢"+ city + "这个城市！")
```

## 使用continue跳过本次循环开始下一次循环

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
    
"""
1
3
5
7
9
"""
```

## 使用 while 循环来处理列表和字典

> for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以
跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。


### 列表之间移动数据

```python
unconfirmed_users = ["王五", "张三", "赵六"]
confirmed_users = []

while unconfirmed_users:
    verify_user = unconfirmed_users.pop()
    print('验证用户：' + verify_user)
    confirmed_users.append(verify_user)

print("所有用户验证完毕")
print("验证成功用户" + str(confirmed_users))
```

### 删除包含特定值的所有列表元素

> 我们使用函数remove()来删除列表中的特定值，这之所以可行，是因为要删除
的值在列表中只出现了一次。如果要删除列表中所有包含特定值的元素，该怎么办呢？

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)

'''
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
'''
```