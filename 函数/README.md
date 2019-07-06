# 函数

## 定义函数

> 函数是带名字的代码块，用于完成具体的工作。

e.g. [greeter.py](greeter.py)
```python
def greet_user():
    """显示简单的问候语"""
    print("Hello")


greet_user()
```

## 向函数传递信息

> 向函数传递参数

e.g. [greetings.py](greetings.py)
```python
def greet_user(user_name):
    """显示简单的问候语"""
    print("Hello " + user_name)


greet_user("John")
```

> 在函数greet_user()的定义中，变量user_name是一个形参——函数完成其工作所需的一项信息。在代码greet_user('John')中，值'John'是一个实参。实参是调用函数时传递给函数的信息。我们调用函数时，将要让函数使用的信息放在括号内。在greet_user('John')中，将实参'John'传递给了函数greet_user()，这个值被存储在形参user_name中。

## 传递实参

> 鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参
的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同；也可使用关键字实参，其
中每个实参都由变量名和值组成；还可使用列表和字典。下面来依次介绍这些方式。

### 位置实参

> 你调用函数时， Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。 为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参

e.g. [pets.py](pets.py)

```python
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\n我有一只" + animal_type + ".")
    print("我的" + animal_type + "的名字叫" + pet_name + ".")


describe_pet("狗", "豆豆")
```

> 调用describe_pet()时，需要按顺序提供一种动物类型和一个名字。


### 关键字实参

> 关键字实参是传递给函数的名称—值对。你直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆。关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。

e.g. [person.py](person.py)

```python
def describe_person(name, age):
    print("你好，我" + str(age) + "岁的朋友，" + name)


describe_person(age=12, name='王五')

describe_person(name="赵六", age=30)
```

> 注意 使用关键字实参时，务必准确地指定函数定义中的形参名。

### 默认值

> 编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时， Python将使用指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。

e.g. [pet.py](pet.py)
```python
def describe_pet(pet_name, animal_type='狗'):
    """显示宠物信息"""
    print("\n我有一只" + animal_type + ".")
    print("我的" + animal_type + "的名字叫" + pet_name + ".")


describe_pet("豆豆")
```

> 请注意，在这个函数的定义中，修改了形参的排列顺序。由于给animal_type指定了默认值，无需通过实参来指定动物类型，因此在函数调用中只包含一个实参——宠物的名字。然而，Python依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，这个实参将关联到函数定义中的第一个形参。这就是需要将pet_name放在形参列表开头的原因所在。

### 可选参数

> 有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息。可
使用默认值来让实参变成可选的。

e.g. [get_formatted_name.py](get_formatted_name.py)

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回姓名"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

### 任意数量的实参

> Python允许函数从调用语句中收集任意数量的实参。

e.g. [pizza.py](pizza.py)

```python
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 使用任意数量的关键字实参

> 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种
情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。

e.g. [user_profile.py](user_profile.py)

```python
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
```

### 等效的函数调用

e.g. [pet.py](pet.py)
```python
def describe_pet(pet_name, animal_type='狗'):
    """显示宠物信息"""
    print("\n我有一只" + animal_type + ".")
    print("我的" + animal_type + "的名字叫" + pet_name + ".")


describe_pet("豆豆")
describe_pet(pet_name="豆豆")
describe_pet("豆豆", "狗")
describe_pet(pet_name="豆豆", animal_type='狗')
describe_pet(animal_type='狗', pet_name='豆豆')
```

> 注意 使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。使用对你来说最容易理解的调用方式即可。

## 返回值

> 函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回
的值被称为返回值。在函数中，可使用return语句将值返回到调用函数的代码行。返回值让你能
够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

e.g. [formatted_name.py](formatted_name.py)

```python
def get_formatted_name(first_name, last_name):
    """返回名字"""
    full_name = first_name + " " + last_name
    return full_name.title()


person = get_formatted_name("John", "ma")
print(person)
```

## 向函数中传递列表

### 在函数中修改列表

> 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的

e.g. [printing_models.py](printing_models.py)

```python
def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

### 禁止函数修改列表

> 有时候，需要禁止函数修改列表。例如，假设像前一个示例那样，你有一个未打印的设计列
表，并编写了一个将这些设计移到打印好的模型列表中的函数。你可能会做出这样的决定：即便
打印所有设计后，也要保留原来的未打印的设计列表，以供备案。但由于你将所有的设计都移出
了unprinted_designs，这个列表变成了空的，原来的列表没有了。为解决这个问题，可向函数传
递列表的副本而不是原件；这样函数所做的任何修改都只影响副本，而丝毫不影响原件。

要将列表的副本传递给函数，可以像下面这样做：

```
function_name(list_name[:])
```

## 将函数存储在模块中

> 函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让
主程序容易理解得多。你还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导
入到主程序中。 import语句允许在当前运行的程序文件中使用模块中的代码

### 导入整个模块

> 导入模块，该模块必须处于python包之下，即文件夹中必须有个`__init__.py`文件，即使该文件为空。这才是一个python包。

```python
import pizza

pizza.make_pizza(14, 'mushrooms', 'green peppers', 'extra cheese')

"""
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese

Making a 14-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
"""
```

### 导入特定的函数

> 你还可以导入模块中的特定函数，这种导入方法的语法如下：

```
from module_name import function_name
```

> 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：

```
from module_name import function_0, function_1, function_2
```

> 对于前面的making_pizzas.py示例，如果只想导入要使用的函数，代码将类似于下面这样：

```
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

> 若使用这种语法，调用函数时就无需使用句点。由于我们在import语句中显式地导入了函数make_pizza()，因此调用它时只需指定其名称。

### 使用 as 给函数指定别名

> 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短
而独一无二的别名——函数的另一个名称，类似于外号。要给函数指定这种特殊外号，需要在导
入它时这样做。

```python
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

> 指定别名的通用语法如下：

```
from module_name import function_name as fn
```

### 使用 as 给模块指定别名

> 你还可以给模块指定别名。通过给模块指定简短的别名（如给模块pizza指定别名p），让你
能够更轻松地调用模块中的函数。

```python
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 导入模块中的所有函数

> 使用星号（*）运算符可让Python导入模块中的所有函数

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

> 注意：最好不要使用这种方式导入函数
