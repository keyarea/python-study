#!/usr/bin/env python3

"""
关键字实参
"""


def describe_person(name, age):
    print("你好，我" + str(age) + "岁的朋友，" + name)


describe_person(age=12, name='王五')

describe_person(name="赵六", age=30)
