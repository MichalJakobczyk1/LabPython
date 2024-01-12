import time

def time_decorator(decorated_function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = decorated_function(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {decorated_function.__name__}: {execution_time} seconds")
        return result
    return wrapper

@time_decorator
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

@time_decorator
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

result_iterative = factorial(1000)
result_recursive = factorial_recursive(10)
