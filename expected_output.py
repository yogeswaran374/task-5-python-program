"""expected output of following python code given """

#usual method tried

data = [10,501,22,37,100,999,87,351]

expected_result = lambda x  : x > 4

result = list(filter(expected_result, data))

print(result)

#code given in the link

result = filter(lambda x: x > 4, data)
print(list(result))

