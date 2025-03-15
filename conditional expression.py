# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a  condition
#                          x if condition else y

num = 5
a = 6
b = 7
age = 25
temperature = 35
user_role = "Guest"

#print("Positive" if num > 0 else "Negative")
#result = "EVEN" if num % 2  == 0 else "ODD"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
#weather = "HOT" if temperature >= 21 else "COLD"
acess_level = "Full Access" if user_role == "Admin" else "Limited Access"


#print(min_num, max_num, status,result,weather)
print(acess_level)