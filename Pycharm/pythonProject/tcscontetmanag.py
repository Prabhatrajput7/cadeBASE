# class Check():
#     def __init__(self,name,mode):
#         self.name = name
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.name,self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
# with Check('testing.txt','w') as f:
#     f.write('HEHEHE')
#
# print(f.closed)


from contextlib import contextmanager
# @contextmanager
# def check(d,m):
#     file = open(d,m)
#     yield file
#     file.close()
#
# with check('testing2.txt','w') as f:
#     f.write('Hell yeah')
#
# print(f.closed)


import os
#
# cwd = os.getcwd()
# os.chdir('venv')
# print(os.listdir())
# os.chdir(cwd)
#
# cwd = os.getcwd()
# os.chdir('__pycache__')
# print(os.listdir())
# os.chdir(cwd)


# @contextmanager
# def filee(d):
#     try:
#         cwd = os.getcwd()
#         os.chdir(d)
#         yield
#     finally:
#         os.chdir(cwd)
#
# with filee('venv'):
#     print(os.listdir())

@contextmanager
def file(s,m):
    f = open(s,m)
    yield f
    f.close()

with file('xxx.txt','w') as g:
    g.write('Hello')