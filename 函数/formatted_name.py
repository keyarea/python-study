#!/usr/bin/env python3


def get_formatted_name(first_name, last_name):
    """返回名字"""
    full_name = first_name + " " + last_name
    return full_name.title()


person = get_formatted_name("John", "ma")
print(person)

