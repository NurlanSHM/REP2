# format specifiers = {value:flags} fromat a value based on what 
#                                       flags are inserted
#
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator


price1 = 3000.14159
price2 = -9870.64
price3 = 1200.34

#print(f"Price 1 is ${price1:.2f}")
#print(f"Price 2 is ${price2:.2f}")
#print(f"Price 3 is ${price3:.2f}")


#SPACE ALLOCATION
#print(f"Price 1 is ${price1:10}")
#print(f"Price 2 is ${price2:10}")
#print(f"Price 3 is ${price3:10}")


#ZERO PAD
#print(f"Price 1 is ${price1:010}")
#print(f"Price 2 is ${price2:010}")
#print(f"Price 3 is ${price3:010}")


#LEFT JUSTIFY
#print(f"Price 1 is ${price1:<10}")
#print(f"Price 2 is ${price2:<10}")
#print(f"Price 3 is ${price3:<10}")



#RIGHT JUSTIFY
#print(f"Price 1 is ${price1:>10}")
#print(f"Price 2 is ${price2:>10}")
#print(f"Price 3 is ${price3:>10}")


#CENTER ALIGN
#print(f"Price 1 is ${price1:^10}")
#print(f"Price 2 is ${price2:^10}")
#print(f"Price 3 is ${price3:^10}")


#DISPLAY POSITIVE
#print(f"Price 1 is ${price1:+}")
#print(f"Price 2 is ${price2:+}")
#print(f"Price 3 is ${price3:+}")


#THOUSANDS SEPERATOR
#print(f"Price 1 is ${price1:,.2fw}")
#print(f"Price 2 is ${price2:,.2f}")
#print(f"Price 3 is ${price3:,.2f}")


