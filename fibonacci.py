import time

cache = {}

def fibonacci(n):
    global cache
    if n in cache:
        return cache[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

start = time.time()

for i in range(0, 101):
    result = fibonacci(i)
    print(i, result)

finish = time.time()
duration = finish - start
print('Вычислили все 100 чисел за', duration, 'секунды')
