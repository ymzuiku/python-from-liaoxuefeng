import os
import shutil
import stat
import json


# 查看系统信息
# print(os.uname())
# 环境变量
# print(os.environ)
# print(os.environ.get('PATH'))

# 查看当前程序执行的路径, 相对
# print(os.path.abspath('.'))
# print(os.path.abspath('../learn-js'))

# 执行shell命令
# os.system('touch bbbbbbbbb')

# 也可以用 join 拼接路径
testTemp = os.path.abspath('./base')
testDir = os.path.join(testTemp, 'testOSDir')

# 查看路径是否存在
os.path.exists(testDir)

# 修改权限, stat.S_IRWXU=所有权限
os.chmod(testDir, stat.S_IRWXU)

# 切换当前路径
# os.chdir('./')

# 读取文件属性
print(os.stat(testDir+'/aa'))

# 创建文件
# f = open(testDir+'/testPickle', 'w')
# f.close()
# 创建目录
# os.mkdir(testDir)
# 创建多级目录
# os.makedirs(testDir+'/bb2/cc/dd/ee')
# 删除文件夹
# os.rmdir(testDir)

# 修改文件名
# os.rename(testDir+'/bb', testDir+'/cc')
# 删除文件
# os.remove(testDir+'/cc')
# 删除文件夹
# shutil.rmtree(testDir+'/testdir')

# 移动文件或目录
# shutil.move(testDir+'/aa', testDir+'/aa_move')
# shutil.move(testDir+'/testdir', testDir+'/testdir-move')
# 复制文件
# shutil.copy(testDir+'/aa', testDir +'/aa_copy')
# 复制目录
# shutil.copytree(testDir+'/testdir', testDir +'/testdir2')


# 分离文件路径和扩展名
print(os.path.splitext(testDir+'/bb/file.bbb.png'))

# 遍历文件夹
for f in os.listdir(testDir):
    if os.path.isfile(testDir+'/' + f) and os.path.splitext(f)[1] == '.py':
        print(f)
    if os.path.isdir(testDir+'/'+f):
        print(f)


# 序列化 反序列化 (就是对象本地存储和读取)

import pickle
d = dict(name='pickle', age=20, score=80)

# 对象转 bytes
print(pickle.dumps(d))

# 序列化 wb表示以bytes的写模式
f = open(testDir+'/testPickle', 'wb')
pickle.dump(d, f)
f.close()

# 反序列化
f = open(testDir + '/testPickle', 'rb')
print(pickle.load(f))
f.close()


# 使用json 序列化

d = dict(name='json', age=20, score=80)
j = json.dumps(d)
f = open(testDir+'/testJson', 'w')
f.write(j)
f.close()

f = open(testDir+'/testJson', 'r')
print(json.loads(f.read()))
f.close()