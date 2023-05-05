#! /usr/bin/env
# _*_ coding: utf-8 _*_
# 时间: 2023-05-05

import time

def run_time(func):
    def wappper(*args, **kwargs):
        print(func.__name__.center(60, "*"))
        t1 = time.perf_counter()
        ret = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"Run time: {t2-t1:.3f}s")
        print(func.__name__.center(60, "*"))
        print()
        return ret
    return wappper

@run_time
def test():
    import random
    li = [random.randint(0, 10000) for _ in range(150000)]
    li.sort()
    print("列表顺序: ", li)

if __name__ == "__main__":
    test()