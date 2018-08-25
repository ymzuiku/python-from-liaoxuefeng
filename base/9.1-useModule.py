import sys
sys.path.insert(0, './')


# 当前文件直接用import
import modules
modules.test()

# 引入其他文件夹,需要在文件夹中创建一个空的 __init__.py 文件
from subModules import useFaterModule
useFaterModule.test3Func()

# 引入其他文件夹所有文件,在__init__.py中这么编写
# from . import modules2
# from . import test3
import subModules

subModules.modules2.test2()


# 引入上级, 需要先用 sys.path.insert(0, './')
# 设置根目录为项目索引第一项,然后就可正常引入了
# 设置了sys.path.insert(0, './')之后就可以很方便的引入各级目录
# 每个文件夹内都要有__init__.py 并且都 from . import xxx 了文件
import modules_fater
modules_fater.modules_fater_file.testFaterModules()

from subModules import subsub
subsub.subsub_file.testSubSubFunc()

import secondModule
secondModule.secondModule_file.testSecondModuleFunc()
