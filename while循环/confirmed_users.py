#!/usr/bin/env python3

unconfirmed_users = ["王五", "张三", "赵六"]
confirmed_users = []

while unconfirmed_users:
    verify_user = unconfirmed_users.pop()
    print('验证用户：' + verify_user)
    confirmed_users.append(verify_user)

print("所有用户验证完毕")
print("验证成功用户" + str(confirmed_users))