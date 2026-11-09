ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set =  {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Mutable
ft_list.append("World!")

ft_set.remove("tutu!")
ft_set.add("Mulhouse")

ft_dict["Hello"] = "42Mulhouse!"


# immutable 
ft_tuple = ft_tuple[:1] + ("France!",)

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

#>python Hello.py | cat -e
#['Hello', 'World!']$
#('Hello', 'France!')$
#{'Hello', 'Paris!'}$
#{'Hello': '42Paris!'}$
