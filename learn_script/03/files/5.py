#!/usr/bin/python

print("main 1")

def function1():
    print("function1")
    function3()

print("main 2")

def function2():
    print("function2")

function2()
print("main 3")

def function3():
    print("function3")

function1()