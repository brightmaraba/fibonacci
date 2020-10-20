import time
def fib(n):
	assert (isinstance(n, int))
	assert (n > 0)
	if n == 1 or n == 2:
		return 1
	else:
		print(n, sep=",", end=" ")
		return fib(n-1) + fib(n-2)



if __name__ == "__main__":
	start_1 = time.time()
	fib_1 = fib(2)
	stop_1 = time.time()
	delta_1 = stop_1 - start_1
	print(delta_1)
	print("++++++++++++++++++++++++++++++++")
	print("++++++++++++++++++++++++++++++++")
	start_2 = time.time()
	fib_2 = fib(50)
	stop_2 = time.time()
	delta_2 = stop_2 - start_2
	print(delta_2)
	print("++++++++++++++++++++++++++++++++")
	print("++++++++++++++++++++++++++++++++")
	delta = (stop_2 - start_2) - (stop_1 - stop_2)
	print(f"Delta : {delta}")
	print("++++++++++++++++++++++++++++++++")
	print("++++++++++++++++++++++++++++++++")

