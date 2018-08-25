
# 循环
sum = 0

i = 0
while i < 100:
    if i > 50:
        break
    i += 1
    sum += i
print(sum)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = list(range(0, 5))
for x in arr:
    sum += x
print(sum)

for v in range(1, 6):
    print(v)

# [最后计算出来的值 for 数组取来的值 in 数组], 然后合并最后计算出来的值
arr2 = [x*x for x in range(1, 11)]
for v in arr2:
    print(v)

arr3 = []
for v in [m+n for m in 'abc' for n in 'zxy']:
    arr3.append(v)
print(arr3)

import os
arr4 = [d for d in os.listdir('./基础')]
print(arr4)

arr5 = [s.lower() for s in ['Hello', 'Dog']]
print(arr5)


# 类似三目运算
three = 100 if 100 > 200 else 200
print(three)


arr6 = [s.lower() if isinstance(s, str) else s for s in [
    'Hello', 18, None, 'dog']]
print(arr6)


# generator 括号代替[], 节约内存,每次使用next()才继续下一步
gen = (x * x for x in range(10))
print(next(gen))
print(next(gen))
for n in gen:
    print(n)
