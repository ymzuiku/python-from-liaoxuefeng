# 普通数组
arr = ['aa', 'bb', 200, 'dd']

print(arr)
print(len(arr))
print(arr[1])
print(arr[-1])
arr.insert(1, '111')
arr.pop()  # 删除最后一个
arr.pop(-1)  # 删除最后一个
arr.pop(0)  # 删除开始第0个
print(arr)

# 不可变
tup = ('aa', 'bb', 'cc')
tup2 = ('aa',)
# tup[1]= 'bbbb' #错误,不可变
print(tup[1])
# print(tup2[1])


# set 不重复的数组

s = set([1, 2, 3, 5, 1, 2, 55])
print(s)
s.add(100)
s.add(2)
s.remove(55)
print(s)

s1 = set([1, 2, 3, 4, 5])
s2 = set([2, 5, 100])
print(s1 & s2)
print(s1 | s2)