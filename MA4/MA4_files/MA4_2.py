#!/usr/bin/env python3


# KVAR TILL NÄSTA PRESENTATION
#fib 47 ger konstigt svar i c++, varför?
#presentera figurer

import matplotlib.pyplot as plt
from integer import Integer
from fibfunctions import fib_pure_py
from fibfunctions import fib_numba_py
from time import perf_counter as pc


def main():
	pure_py_times = []
	numba_py_times = []
	c_integer_times = []
	
	######### N = 30:45 #########
	n_range = range(20, 35)
	for i in n_range:
		start = pc()
		print('pure fib of ', i, ': ', fib_pure_py(i))
		end = pc()
		pure_py_times.append(end-start)	
			
		# start = pc()
		# fib_numba_py(i)
		# end = pc()
		# numba_py_times.append(end-start)

		f = Integer(i)
		start = pc()
		f.fib()
		end = pc()
		c_integer_times.append(end-start)
			
	plt.plot([*n_range], pure_py_times, label = 'pure py fib')
	# plt.plot([*n_range], numba_py_times, label = 'numba py fib')
	plt.plot([*n_range], c_integer_times, label = 'C++ fib')
	plt.xlabel('n')
	plt.ylabel('time (s)')
	plt.legend()
	plt.savefig('fib_plot.png')
	
	######### N = 1:30 #########
	# n_range2 = range(1, 31)
	# for i in n_range2:
	# 		start = pc()
	# 		print('pure fib of ', i, ': ', fib_pure_py(i))
	# 		end = pc()
	# 		pure_py_times.append(end-start)	
				
	# 		start = pc()
	# 		fib_numba_py(i)
	# 		end = pc()
	# 		numba_py_times.append(end-start)

	# plt.plot([*n_range], pure_py_times, label = 'pure py fib')
	# plt.plot([*n_range], numba_py_times, label = 'numba py fib')
	# plt.xlabel('n')
	# plt.ylabel('time (s)')
	# plt.legend()
	# plt.savefig('fib_plot2.png')
		  
	######### FIBONACCI 47 I C++ #########
	# f = Integer(47)
	# f.fib()



if __name__ == '__main__':
	main()