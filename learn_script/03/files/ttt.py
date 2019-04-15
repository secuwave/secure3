# content of test_expectation.py
# -*- encoding: utf-8 -*-


def t1():
    val = 1
    r = val > 0 and 'pos'
    print("r = {}".format(r))


def t2():
    # s = [1,2,3]
    s = []
    first_char = s and s[0]
    print("first_char = {}".format(first_char))


def t3():
    x = None
    safe_x = x or 0
    print("safe_x = {}".format(safe_x))


if __name__ == '__main__':
    # t1()
    t2()
    t3()
