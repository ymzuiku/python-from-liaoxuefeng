import unittest

class TestDict(unittest.TestCase):
    # 当测试刚开始时会使用 setUp 方法
    def setUp(self):
        print('setup...')
    # 当测试结束时会使用 tearDown 方法

    def tearDown(slice):
        print('teardown...')

    def test_init(self):
        d = {'a': 1, 'b': 'test'}
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 'test')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')


class Testb(unittest.TestCase):
    def test_bb(self):
        self.assertEqual(1, 1)


# 加上这两行,程序运行这个脚本时,就会使用 unittest.main()
if __name__ == '__main__':
    unittest.main()

