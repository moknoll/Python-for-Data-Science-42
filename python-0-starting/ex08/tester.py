from ft_filter import ft_filter

print(list(ft_filter(lambda x: x > 5, [2, 7, 3, 9])))
print(list(ft_filter(None, [0, 1, 2, 0])))
print(list(ft_filter(lambda x: x, [])))
print(list(ft_filter(None, ["", "Hello", "World"])))
print(list(ft_filter(lambda x: x % 2 == 0, range(10))))
print(filter.__doc__ == ft_filter.__doc__)