# 条件判断
age = "20"
age = int(age)  # 类型转化
if age > 18:
    print('ok')
    print(age)

if not age > 100:
    print('< 100')

# 空内容,占位 pass
if age > 100:
    pass

if age > 200:
    print('ok')
    print(age)
elif age >= 6:
    print('>6')
else:
    print('err')

