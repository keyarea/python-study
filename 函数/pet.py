#!/usr/bin/env python3

"""
默认值
"""


def describe_pet(pet_name, animal_type='狗'):
    """显示宠物信息"""
    print("\n我有一只" + animal_type + ".")
    print("我的" + animal_type + "的名字叫" + pet_name + ".")


describe_pet("豆豆")
describe_pet(pet_name="豆豆")
describe_pet("豆豆", "狗")
describe_pet(pet_name="豆豆", animal_type='狗')
describe_pet(animal_type='狗', pet_name='豆豆')