# This program is "NUMBER GUESSING GAME", have fun using it!
import random
rnum = random.randint(1,100)
query = True
# print(rnum)
count = 0

while query:
  number = int(input("Enter any number 1-100 inclusively: "))
  count += 1
  if number > rnum:
    if number - rnum >= 30:
      print("Uhoo! come down by a lot..somewhere 20 or 40 or 60.")
    elif number - rnum > 10:
      print("Yeah-Yeah, you are close.")
    else:
      print("Yeah..yeah..super close, go down a bit, one digit number..")

  elif rnum > number :
    if rnum - number >= 30:
      print("Buddy! you need to leap a lot , maybe 20...30...40.")
    elif rnum - number > 10:
      print("You are close, rise up maybe near 12, 15, 18.")
    else:
      print("Super close...rise up in one digit number..")

  else:
    print("Tada..You are correct. The number was",rnum,"in",count,"tries.")
    query = False