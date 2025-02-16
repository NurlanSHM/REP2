
numpad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ('*',0,'#'))

for i in numpad:
    for x in i:
        print(x, end=" ")
    print()