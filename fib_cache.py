import time
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(input_value):
    if input_value == 1:
        return 1
    elif input_value == 2:
        return 1
    elif input_value > 2:
        return fibonacci(input_value -1) + fibonacci(input_value -2)



if __name__ == "__main__":
    start_time = time.time()
    print(fibonacci(500))
    fin_time = time.time()
    print(fin_time - start_time)
