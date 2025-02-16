# Concession stand program

menu = {"Pizza": 3.00,
        "Nachos": 4.50,
        "Popcorn": 5.50,
        "Fries": 2.00,
        "Crisps": 1.00,
        "Pretzel": 1.50,
        "Soda": 0.50,
        "Lemonade": 2.45}

cart = []
total = 0.0

print("---------MENU---------")
for k,v in menu.items():
    print(f"{k:10}: £{v:.2f}")
print("-----------------------")

while True:
    food = input("Select an item(Q to Quit): ").title()
    if food == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    
print("-------YOUR ORDER------")
for f in cart:
    total += menu.get(f)
    print(f , end=" ")

print()
print(f"Total is: £{total:.2f}")