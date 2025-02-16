
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

for i in groceries:
    for x in i:
        print(x, end=" ")

#print(groceries[0][1])
