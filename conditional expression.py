# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a  condition
#                          x if condition else y

num = 5
a = 6
b = 7
age = 25

#print("Positive" if num > 0 else "Negative")
#result = "EVEN" if num % 2  == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b


print(max_num)