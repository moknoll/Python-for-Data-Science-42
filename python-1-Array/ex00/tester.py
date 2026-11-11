from give_bmi import give_bmi, apply_limit

# Test 1 correct values
print("Test 1: ")
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("Test 2: ")
height2 = ["hello", 2.2]
weight2 = [123.3, 123.3, 123.5]
bmi = give_bmi(height2, weight)

print("Test 3: ")
bmi = give_bmi(height2, weight2)
apply_limit(bmi, -2)
