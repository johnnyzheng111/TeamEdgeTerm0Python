# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
    #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------

drink_price = 0
meal_price = 0
dessert_price = 0
total_price = drink_price + meal_price + dessert_price
total_people = 3
tax = 0.0725 # california sales tax 
tip = 0.15
each_person_pays = (total_price + tax + tip) / total_people
item_price = 0
item_name = ""
# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------

meal_menu = ["Steak", "Spaghetti", "Pizza", "Burgers"]
meal_price = [29.99, 14.99, 14.99, 9.99]

drink_menu = ["Coke", "Wine", "Beer", "Lemonade"]
drink_price = [2.99, 29.99, 7.99, 4.99]

dessert_menu = ["Cake", "Ice Cream", "Cupcake", "Macaroons"]
dessert_price = [15.99, 6.99, 3.99, 6.99]

def print_menu(): 
  print("Meals:")
  print("-----------------------------")
 
  for i in range(len(meal_menu)): 
    print(meal_menu[i] + " Price: $" + str(meal_price[i]))
    
  print("Drinks:")
  print("-----------------------------")
  for i in range(len(drink_menu)):
    print(drink_menu[i] + " Price: $" + str(drink_price[i]))
  print("Desserts:")
  print("-----------------------------")
  for i in range(len(dessert_menu)): 
    print(dessert_menu[i] + " Price: $" + str(dessert_price[i]))
  print("-----------------------------")


# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------
order_type = input("What would you like to order ? A Meal, Dessert, or a Drink?")
# Should be a Meal, Drink, or Dessert
order = input("Awesome! Pick an item from the list above.")
item_name = order


def take_order(): 
  if str(order_type) == "Meal": 
    for i in range(len(meal_menu)): 
      if(order == meal_menu[i]): 
        return float(meal_price[i])
      else: 
        return -1
  elif str(order_type) == "Drink": 
    for i in range(len(drink_menu)): 
      if(order == drink_menu[i]): 
        return float(drink_price[i])
      else: 
        return -1
  elif str(order_type) == "Dessert":
    for i in range(len(dessert_menu)): 
      if(order == dessert_menu[i]): 
        return float(dessert_price[i])
      else: 
        return -1
  else: 
    print("please enter a valid order!")
    return -1
    











# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 
def cost_of_order(): 
  tip = input("How much would you like to tip? ex. 15% would be 0.15.")
  tip = float(tip)
  tip_amount = tip * total_price
  tax_amount = tax * total_price
  # print("Cost of all ordered items: " str(total_price))
  return "Total Cost of the order: " + str(total_price + tax_amount + tip_amount)







# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 

def print_receipt(item_name, item_price): 
  print("Cost of each item: ")
  print("Item Price: " + str(item_price))
  print("Item Name: " + str(item_name))
  print("Tax: " + str(tax * item_price))
  print("Tip: " + str(tip * item_price))
  



# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------

print_menu()

price = take_order()
item_price = price
total_price += price
print(price)

print(cost_of_order())

print_receipt(item_name, item_price)



# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------

