# Python Compound Interest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Invalid Principle. Cannot be 0 or less than 0.")
    else:
        break

while True:
    rate = float(input("Enter the Interest Rate: "))
    if rate <= 0:
        print("Invalid Interest Rate. Cannot be 0 or less than 0.")
    else:
        break

while True:
    time = int(input("Enter the time (in years): "))
    if time <= 0:
        print("Invalid Time. Cannot be 0 or less than 0.")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f} ")
