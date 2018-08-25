# 文档测试的好处是可以直接把测试内容写在代码里
# doctest非常有用，不但可以用来测试，还可以直接作为示例代码。
# 通过某些文档生成工具，就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。

def abs(n):
    """ 
    文档测试,多行注释的代码也可以运行

    >>> abs(1)
    1
    >>> abs(-2) #这行是错的,会打印出来
    1
    """
    return n if n >= 0 else (-n)


# 这几行的意思是,只有直接执行这个文件,才执行 doctest.testmod()
if __name__ == '__main__':
    import doctest
    doctest.testmod()
