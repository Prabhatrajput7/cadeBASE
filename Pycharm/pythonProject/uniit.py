# python -m unittest to run all unit test lets say 2 have 2 unittest files each with 4 tc then
# python -m unittest will execute 8 tc
# python -m unittest - v (verbos)

import unittest
import uniitsu

class Testmain(unittest.TestCase):
    def setUp(self) -> None:
        print('About to test a FX')  # run before any fx runs
    def test_do_stuff(self):
        '''HII'''
        num = 10
        result = uniitsu.do_stuff(num)
        self.assertEqual(result,15)

    def test_do_stuff2(self):
        num = 'abcd'
        result = uniitsu.do_stuff(num)
        self.assertTrue(isinstance(result,ValueError))

    def test_do_stuff3(self):
        num = None
        result = uniitsu.do_stuff(num)
        self.assertEqual(result,'enterNOPLZ')

    def test_do_stuff4(self):
        num = ''
        result = uniitsu.do_stuff(num)
        self.assertEqual(result,'enterNOPLZ')

    def test_do_stuff5(self):
        num = 0
        result = uniitsu.do_stuff(num)
        self.assertEqual(result,'enterNOPLZ')

    def tearDown(self) -> None:
        print('done')

if __name__ == '__main__':
    unittest.main()#it only means run all the TC