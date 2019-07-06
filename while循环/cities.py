#!/usr/bin/env python3

message = "\n请输入你曾经去过的城市:"
message += "\n当你输入完毕，输入quit结束程序"

while True:
    city = input(message)

    if city == 'quit':
        break
    else:
        print("我喜欢"+ city + "这个城市！")
