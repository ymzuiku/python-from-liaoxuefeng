# 多线程

# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享

import time
import threading

balance = 0
lock = threading.Lock()

def change_it(n):
    # 共享不同线程的变量
    global balance
    for i in range(500):
        balance = balance + i
    for i in range(500):
        balance = balance - i
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(5000):
        change_it(n)

def run_threadLock(n):
    for i in range(500):
        # 启动一个锁,其他线程会排队
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()


# 500个thread
run = run_threadLock
t1 = threading.Thread(target=run, args=(5,))
t1.start()
t2 = threading.Thread(target=run, args=(6,))
t2.start()
t3 = threading.Thread(target=run, args=(7,))
t3.start()
t1.join()
t2.join()
t3.join()

# run_thread结果不是0 run_threadLock是0
print(balance)
