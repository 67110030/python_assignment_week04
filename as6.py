grades = [55, 70, 65, 40, 90, 85, 50, 77]
passed_with_bonus = lambda x: x + 10 if x > 60 else False
print(list(filter(passed_with_bonus, grades)))