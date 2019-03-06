#!/usr/bin/env python3
import timeit
def addnumber():
	1+1
print(timeit.timeit(stmt=addnumber,number=100000000))
