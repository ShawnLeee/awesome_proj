# encoding: utf-8
import ctypes
import os
import sys

_file = 'libsimple.so'
_path = os.path.join(*(os.path.split(__file__)[:-1] + ('libsimple.so',)))
_mod = ctypes.cdll.LoadLibrary(_path)

#int add(int , int)
add = _mod.add
add.argtypes = (ctypes.c_int, ctypes.c_int)
add.restype = ctypes.c_int



ThreadFunc = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

start_thread = _mod.xa_start_thread
start_thread.argtypes = [ThreadFunc, ctypes.c_void_p]
start_thread.restype = ctypes.c_int


def py_thread_func():
    print('thread_func')
    return None

thread_func = ThreadFunc(py_thread_func)

thread_test = _mod.thread_test
thread_test.argtypes = [ctypes.c_int]
thread_test.restype = ctypes.c_int

thread_test(2)

