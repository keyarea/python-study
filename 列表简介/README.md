# 列表简介

## 列表是什么

> 列表由一系列按特定顺序排列的元素组成。

> 鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如letters、 digits或names）是
个不错的主意。

> 在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。

e.g. 一个普通的列表

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers)  #  [1, 2, 3, 4, 5, 6, 7, 8]
```

## 访问列表元素

> 列表是有序集合，因此要访问列表的任何元素，只需知道该元素的位置或索引

e.g. 访问其中一个元素

```python
books = ["javascript高级程序设计", "第一行代码", "python基础"]
print(books[2])  # python基础
```

> 第一个列表元素的索引为0，而不是1。在大多数编程语言中都是如此。

e.g. Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让Python返
回最后一个列表元素

```python
books = ["javascript高级程序设计", "第一行代码", "python基础"]
print(books[2])  # python基础
print(books[-1]) # python基础
```

## 修改添加删除元素

> 你创建的大多数列表都将是动态的，这意味着列表创建后，将随着程序的运行增删元素。

### 修改列表元素

e.g. 

```python
cars = ["玛莎拉蒂", "奔驰", "凯迪拉克", "大众"]
print(cars)  # ["玛莎拉蒂", "奔驰", "凯迪拉克", "大众"]
cars[0] = "路虎"
print(cars)  # ['路虎', '奔驰', '凯迪拉克', '大众']
```

### 添加列表元素

#### 实例方法：append()

> 将元素附加到列表的末尾

e.g. 
```python
phones = ["三星", "苹果"]
phones.append("小米")
print(phones) # ['三星', '苹果', '小米']
```

#### 实例方法：insert()

> 在列表中的任意位置插入值

```python
phones = ['三星', '苹果', '小米']
phones.insert(1, "华为")
print(phones) # ['三星', '华为', '苹果', '小米']
```

### 删除列表元素

#### del语句

> 删除指定索引的元素

```python
phones = ['三星', '华为', '苹果', '小米']
del phones[0]
print(phones)  # ['华为', '苹果', '小米']
```

#### 实例方法：pop()

> 将元素从列表中删除，并接着使用它的值

```python
phones = ['华为', '苹果', '小米']

phone = phones.pop()  # 删除列表中的最后一个元素并返回该值
print("为发烧而生的手机: " + phone)  # 为发烧而生的手机: 小米
print(phones)  #  ['华为', '苹果']

apple = phones.pop(1)  # 删除列表中的索引的值，并将其返回
print("堪称奢侈品的手机：" + apple)  #  堪称奢侈品的手机：苹果
print(phones) # ['华为']
```

> 当然这个索引也支持负值，即`instance.pop(-1)`也是删除列表最后一个元素并返回

#### 实例方法：remove()

> 有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使
用方法remove()。

e.g.
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
```

> 注意、方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要
使用循环来判断是否删除了所有这样的值。

## 组织列表

### sort()

> 对列表进行排序，会永久性的改变列表 

```python
letters = ["p", "b", "i", "n", "m"]
letters.sort()
print(letters)  # ['b', 'i', 'm', 'n', 'p']

letters = ["p", "b", "i", "n", "m"]
letters.sort(reverse = True)
print(letters)  # ['p', 'n', 'm', 'i', 'b']
```

### sorted()

> 对列表进行排序，不会影响原列表

```python
letters = ["p", "b", "i", "n", "m"]
print(sorted(letters)) # ['b', 'i', 'm', 'n', 'p']
print(letters)  # ['p', 'b', 'i', 'n', 'm']

letters = ["p", "b", "i", "n", "m"]
print(sorted(letters, reverse = True))  # ['p', 'n', 'm', 'i', 'b']
print(letters)  # ['p', 'b', 'i', 'n', 'm']
```

### reverse()

> 反转列表元素的排列顺序

> 方法`reverse()`永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此
只需对列表再次调用`reverse()`即可。

```python
letters = ["p", "b", "i", "n", "m"]
letters.reverse()
print(letters) # ['m', 'n', 'i', 'b', 'p']
```

### len()

> 函数`len()`可快速获悉列表的长度。

```python
letters = ["p", "b", "i", "n", "m"]
print(len(letters)) # 5
```

## 操作列表

### 遍历列表

e.g. 遍历列表

```python
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
```

### 创建数组列表：`range()`

> Python函数`range()`让你能够轻松地生成一系列的数字。

e.g. 例如，可以像下面这样使用函数`range()`来打印一系列的数字;

```python
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
```

> 注意：函数`range()`让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出
不包含第二个值（这里为10）。


e.g.  要创建数字列表，可使用函数`list()`将`range()的`结果直接转换为列表。

```python
numbers = list(range(1, 10))
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

e.g.  使用函数range()时，还可指定步长。例如，下面的代码打印1~10内的偶数：

```python
numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]
```

> 在这个示例中，函数range()从2开始数，然后不断地加2，直到达到或超过终值（11）

e.g. 对数字数组进行简单的统计

```python
numbers = list(range(2, 11, 2))
print(max(numbers))  # 10
print(min(numbers))  # 2
print(sum(numbers))  # 30
```

e.g. 列表解析

```python
numbers = [value ** 2 for value in range(1, 11)]
print(numbers) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

> 在这个示例中，表达式为`value**2`,它计算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。
> 在这个示例中，for循环为for value in range(1,11)，它将值1~10提供给表达式value**2。

## 列表切片

### 切片

> 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range()一样，Python
在到达你指定的第二个索引前面的元素后停止。要输出列表中的前三个元素，需要指定索引0~3，
这将输出分别为0、 1和2的元素


e.g. 切片实例

```python
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[1:3]) # [2. 3]
print(numbers[:3]) # [1, 2, 3]
print(numbers[:]) # [1, 2, 3, 4, 5, 6, 7]
print(numbers[2:]) # [3, 4, 5, 6, 7]
print(numbers[-3:]) # [5, 6, 7]
```

> `numbers[:]`该方法可以用来复制列表，他会创建一个新的列表。（不过这种方法创建的数组是浅拷贝）

e.g. 切片拷贝的数组是浅拷贝

```python
a = [1, 2, 3, 4, 5, [6, 7, 8]]
b = a[:]
a[-1].append(9)
print(a)  # [1, 2, 3, 4, 5, [6, 7, 8, 9]]
print(b)  # [1, 2, 3, 4, 5, [6, 7, 8, 9]]
```

