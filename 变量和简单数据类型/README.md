# 变量和简单数据类型

## 变量

e.g. 定义一个变量

```python
#!/usr/bin/env python3

# 定义一个变量
message = "hello world"

# 输出该变量
print(message)
```

> 有关变量命名的规则。
> - 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打
头，例如，可将变量命名为message_1，但不能将其命名为1_message。
> - 变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message
可行，但变量名greeting message会引发错误。
> - 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，
如print
> - 变量名应既简短又具有描述性。例如， name比n好， student_name比s_n好， name_length
比length_of_persons_name好。
> - 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。


## 字符串

字符串是一系列的字符，在python中引号括起来的都是字符串。

> 注意：引号可以是单引号也可以是双引号

### 一些方法

#### title() 将每个单词的首字母变为大写

```python
#!/usr/bin/env python3

# 定义了一个字符串
message = "hello world"

# 将每个单词的首字符变为大写
print(message.title())  # Hello World
```

#### upper() 将字符串全部变为大写
#### lower() 将字符串全部变为小写
#### 拼接字符串

e.g. 

```python
# 拼接字符串
first_name = "kai"
last_name = "wang"
full_name = first_name + " " + last_name
print(full_name)  # kai wang
```

#### 使用制表符或换行符来添加空白

在编程中， 空白泛指任何非打印字符，如空格、制表符和换行符。你可使用空白来组织输出，
以使其更易读。

e.g. 

```python
# 添加空白
print("\thello world")
print("hello \nworld")
```

输出：

```
	hello world
hello 
world
```

#### 删除空白

> `strip()` : 删除两侧空白
> `lstrip()` ：删除左侧空白
> `rstrip()` ：删除右侧空白

```python
# 删除空白
two_sides_blank = "  hello  "

del_left_blank = two_sides_blank.lstrip()  # 删除左侧空白
del_right_blank = two_sides_blank.rstrip()  # 删除右侧空白
del_blank = two_sides_blank.strip()  # 删除两侧空白

print(del_left_blank)
print(del_right_blank)
print(del_blank)
```

## 数字

### 整数

```python
#!/usr/bin/env python3

num1 = 1
num2 = 2
num3 = 3

print(num1 + num2)  # 3 加法操作
print(num3 - num1)  # 2  减法操作
print(num3 * num2)  # 6  乘法操作
print(num3 / num2)  # 1.5  除法操作
print(num3 // num2)  # 1  除法操作（该除法操作不会保留小数部分）
print(num3 % num2)  # 1  取余操作
print(num3 ** num2)  # 9  乘方操作

# 括号可以改变运算顺序
print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
```

#### 浮点数

Python将带小数点的数字都称为浮点数。

```python
# 浮点数
print(0.1 + 0.2)  # 0.30000000000000004
print(0.2 - 0.1)  # 0.1
print(0.2 * 0.3)  # 0.06
print(0.3 / 0.2)  # 1.4999999999999998
print(0.3 // 0.2)  # 1.0
print(0.2 ** 0.3)  # 0.6170338627200097
print(0.3 % 0.2)  # 0.09999999999999998
```

> 但需要注意的是，结果包含的小数位数可能是不确定的





