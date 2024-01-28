
"check the given list is string or integer"

data = [10, 12, 13, "string", 17, "data"]

check_int_or_str = lambda x : x == str(x)


result = list(map(check_int_or_str,data))
print(result)

r = list(filter(check_int_or_str,data))
print(r)

