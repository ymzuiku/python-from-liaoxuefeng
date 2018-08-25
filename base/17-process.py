import os

# 进程id
print(os.getpid())
# 线程id
print(os.getppid())

# 只能再 Unix/linux/maxos 中使用
pid = os.fork()

if pid == 0:
    print('master process', os.getpid(), os.getppid())
else:
    print('work process', os.getpid(), os.getppid())


# 包含windows的跨平台
from multiprocessing import process


def run_process(name):
    print('child process %s %s %s' % (name, os.getpid(), os.getppid()))

if __name__ == '__main__':
    p = process()
