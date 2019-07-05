# if语句

条件判断语句

## 逻辑操作符

> - `==`： 是否相等
> - `>`：是否大于
> - `!=`：是否不等于
> - `<`：是否小于
> - `>=`：是否大于等于
> - `<=`：是否小于等于

## 检查多个条件

> - `and` :要检查是否两个条件都为True，可使用关键字and将两个条件测试合而为一；如果每个测试都通过了，整个表达式就为True；如果至少有一个测试没有通过，整个表达式就为False
> - `or`:关键字or也能够让你检查多个条件，但只要至少有一个条件满足，就能通过整个测试。仅当两个测试都没有通过时，使用or的表达式才为False

## 检查特定值是否包含在列表中

> - `in`:要判断特定的值是否已包含在列表中，可使用关键字in。

```
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
```

## 使用not关键字进行取反

> - `not`: 进行取反操作

## if语句

e.g. 

```python
result = "hello"

if result == "hello":
    print("this is hello")
elif result == "world":
    print("this is world")
else:
    print("this is other")
```

## 判断数组是否为空

e.g. 

```python
books = []

if books:
    print(books)
else:
    print("this is empty")
```

