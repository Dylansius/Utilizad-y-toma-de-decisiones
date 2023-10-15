def utility_function(x):
    return -x**2 + 4 * x

values = [1, 2, 3, 4, 5]
utilities = [utility_function(x) for x in values]

print("Valores:", values)
print("Utilidades:", utilities)

