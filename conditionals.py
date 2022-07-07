# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

import random

message = "Welcome to Day 2.\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!"
print(message)
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")
# Can you drive?
   # Prompt the user to enter their 16age.
   # Write conditional statements that print out whether you can drive in your city. 

age = input("Enter your age: ")
print(age)
print(type(age))
if int(age) >= 16:
   print("You can drive!")
else: 
   print("you are not old enough to drive :(")









# -------------------------------------------- 

print("------------------- Challenge 2 -------------------") 

# Who placed first?
   # Write conditional statements that checks which is the highest and prints the highest score. 
   # Hint: Create three variables and assign them random scores. 

score1 = random.randint(1, 20)
score2 = random.randint(1, 20)
score3 = random.randint(1, 20)
print("Generating three random scores from 1 to 20")
print(score1)
print(score2)
print(score3)
highest = max(score1, max(score2, score3))
print("The highest score is " + str(highest))







# -------------------------------------------- 

print("------------------- Challenge 3 -------------------")

# One of the most common parts of our daily routine is checking the weather. 
# Our outfit and accessories are dependent on the temperature and conditions outside. 
# ie. We're probably not going to wear shorts out when it's snowing...


# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# Rainy: Bring an umbrella
# Sunny: Wear a hat and sunglasses
# Snowing: Wear gloves and a scarf 

# Here's a variable to get you started:
weather = "Rainy" # Rainy, Sunny, or Snowy
temperature = 30
if weather == "Rainy" and temperature == 0:
   print("Bring an Umbrella, wear a furry coat and thick pants")
elif weather == "Rainy" and temperature == 30: 
   print("Bring an Umbrella, wear a warmer jacket")
elif weather == "Rainy" and temperature == 60: 
   print("Bring an Umbrella, wear a light jacket")
elif weather == "Sunny" and temperature == 30:
   print("Wear a hat and sunglasses and a light jacket")
elif weather == "Sunny" and temperature == 60:
   print("Wear a hat and sunglasses and a shirt")
elif weather == "Sunny" and temperature == 90:
   print("Wear a hat and sunglasses and a tanktop")
elif weather == "Snowing":
   print("Wear gloves and a scarf")
else: 
   print("Please enter a valid weather and/or temperature")











# Tip: Try changing the value of the weather variable to test your other conditions.

# **** Challenge 3: Part 2 ****
# Now that you've written conditions for specific weather forecasts, let's also add in temperature! 
# You can't dress accordingly if you only know that it's raining outside but not how cold it is!
# For example:
    # If it's raining and 60 degrees, you might want to bring your umbrella and wear a light jacket.
    # However, if it's raining and 30 degrees, you might want to break out a warmer jacket with your umbrella instead. 
    
   # Add to your conditional statements above and modify your weather reports to also take into account the temperature. 
   # Make sure to account for at least three different temperatures!
   # Hint: You will need another variable to keep track of the temperature.













# -------------------------------------------- 

print("------------------- Challenge 4 -------------------")

# Prompt the user to enter the day of the week (1-7 representing Monday - Sunday)
# Write a set of conditionals that will take a number from 1 to 7 
# and print out the corresponding day of the week. 
# Make sure to add a statement that accounts for any numbers out of range! 

dayOfTheWeek = input("Enter in the day of the week, 1-7 representing Mon-Sun: ")
dayOfTheWeek = int(dayOfTheWeek)
print(type(dayOfTheWeek))
if dayOfTheWeek == 1: 
   print("Corresponding day: Monday")
elif dayOfTheWeek == 2: 
   print("Corresponding day: Tuesday")
elif dayOfTheWeek == 3: 
   print("Corresponding day: Wednesday")
elif dayOfTheWeek == 4: 
   print("Corresponding day: Thursday")
elif dayOfTheWeek == 5: 
   print("Corresponding day: Friday")
elif dayOfTheWeek == 6:
   print("Corresponding day: Saturday")
elif dayOfTheWeek == 7:
   print("Corresponding day: Sunday")
else: 
   print("That is not a day of the week! Try again :)")








# -------------------------------------------- 

print("------------------- Challenge 5 -------------------")

# A leap year is a calendar year that contains an additional day added 
# to keep the calendar year synchronized with the astronomical year or seasonal year.
# To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days).
     # 5. The year is not a leap year (it has 365 days).

# Those are a lot of conditions...
# Your challenge is to translate the steps above into conditionals which will evaluate if the 
# year stored in a variable is/was a leap year.

print("Hey what year is it?")
year = input()
year = int(year)

if year % 4 == 0: 
   if year % 100 == 0: 
      if year % 400 == 0: 
         print("This year's a leap year!")
      else: 
         print("This year isn't a leap year.")  
   else: 
      print("This is a leap year!")
else: 
   print("This year is not a leap year.")





