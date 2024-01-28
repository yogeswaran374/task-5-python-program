"create a fibonacci series from 1 to 50"



x =list(range(1,51))


fibonacci_series = lambda i : i if i<=1 else (i-1)+i
result = list(map(fibonacci_series, x))
print(result)

