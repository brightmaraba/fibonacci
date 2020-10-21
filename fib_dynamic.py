import time

fib_array = [0,1]

def fib(n):
    assert(isinstance(n, int))
    assert(n > 0)
    if n <= len(fib_array):
        return fib_array[n-1]
    else:
        temp_fib = fib(n-1) + fib(n-2)
        fib_array.append(temp_fib)
        return(temp_fib)

if __name__ == "__main__":
    start_time = time.time()
    print(fib(500))
    fin_time = time.time()
    print(fin_time - start_time)


