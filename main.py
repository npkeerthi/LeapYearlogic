
y= int(input("Which year do you want to check? "))

if y%4==0:
  if y%100 != 0:
    print(y,"is leapyear")
  elif y%400 == 0:
    print(y,"is leapyear")
  else:
    print(y,"is a non-leapyear")
else:
  print(y,"is non-leapyear")


