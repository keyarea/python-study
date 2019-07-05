# 元组

> Python将不能修改的值称为不可变的，而不可变的列表被称为元组。

> 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来
访问其元素，就像访问列表元素一样。

e.g. 

```python
numbers = (1, 2, 3)

# 访问其元素

print(numbers[0]) # 1

# 遍历

for number in numbers:
    print(number)

'''
1
2
3
'''

# 修改元组变量

numbers = (4, 5, 6)
print(numbers)  # (4, 5, 6)
```

