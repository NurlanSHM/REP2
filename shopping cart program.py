# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (Q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print(" ----- YOUR CART -----")

for i in range(len(foods)):
    print(f"{foods[i]}  ${prices[i]:.2f}")

print("----------------------")

for price in prices:
    total += price

print(f"Total cost: ${total:.2f}")
print("----------------------")