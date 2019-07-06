# 用户输入

## 函数 input()的工作原理

> 函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后， Python将其存储在
一个变量中，以方便你使用。

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

> 函数input()接受一个参数：即要向用户显示的提示或说明，让用户知道该如何做。

## 使用int()来获取数值输入

> 使用函数input()时， Python将用户输入解读为字符串。

```python
age = input("How old are you?")
print(int(age))
```

