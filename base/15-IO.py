
# 相对于程序执行的路径

# w     以写方式打开，
# a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
# r+     以读写模式打开
# w+     以读写模式打开 (参见 w )
# a+     以读写模式打开 (参见 a )
# rb     以二进制读模式打开
# wb     以二进制写模式打开 (参见 w )
# ab     以二进制追加模式打开 (参见 a )
# rb+    以二进制读写模式打开 (参见 r+ )
# wb+    以二进制读写模式打开 (参见 w+ )
# ab+    以二进制读写模式打开 (参见 a+ )

f = open('./base/testio.txt', 'r')
print('test async')
print(f)
# 一次性读取, 不合适大文件,例如100mb就会占用100mb的内存
print(f.read())

# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源
# 并且操作系统同一时间能打开的文件数量也是有限的
f.close()

# 读 with自动关闭
with open('./base/testio.txt', 'r') as f:
    # 按行读取
    for line in f.readlines():
        line.strip()

    # f的内容是空的,因为f关闭了
    print(f.readlines())


# 写
with open('./base/testio.txt', 'w') as f:
    f.write('hello io');

