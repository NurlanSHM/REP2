# logical operators
#               or = atleast one condition must be true
#               and = both conditions must be true
#               not = inverted condition (True = False, and vice versa)


# or (code done and tested, hashtagged items)

#temp = 25
#is_raining = False 

#if temp > 35 or temp < 0 or is_raining:
#    print("The outdoor event is cancelled")

#else:
#    print("The outdoor event is still scheduled")


# and

#temp = -3
#is_sunny = True

#if temp >= 30 and is_sunny:
#    print("It is HOT outside")
#    print("It is SUNNY")

#elif temp <= 0 and is_sunny:
#    print("It is COLD outside")
#    print("It is SUNNY")

#elif 28 > temp > 0 and is_sunny:
#    print("It is WARM outside")
#    print("It is SUNNY")



# not

temp = -3
is_sunny = False

if temp >= 30 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")

elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY")

elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY")
