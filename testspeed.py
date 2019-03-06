!#/usr/bin/env python3
import timeit
def addnumber():
	1+1
timeit.timeit(stmt=addnumber,times=1000000)
