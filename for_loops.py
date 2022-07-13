#********************************************************************
 #                                                                  
 #  Team Edge List Mini-project: FOR LOOP CHALLENGES
 # 
 #   Complete the following loop challenges below. Follow the ToDos
 #   1. COUNTER: Write a loop that prints a happy birthday message for every
 #      year you have been alive.
 #   2. ITERATOR: Write a for for loop that prints every item in a list

 #   3. EVEN COUNTDOWN: Write a for loop that counts down from 100 to 0, 
 #      printing only the odd numers
 #   4. FINDER: Write a function that takes in a list and a word and prints 
 #      CONGRATULATIONS!! if the word is found in the list
 #   5. NESTED: Write a function that logs every letter in a sentence
 # 
 # ***************************************************************/
import random

print("------------------- CHALLENGE 1 : COUNTER -------------------")

#this list prints every number between 0 and 10, using range

for x in range(11):
    print("Counter at: " + str(x))
   

#-->TODO: Write a loop that prints a happy birthday message for every year you have been alive.
for i in range(1, 17): 
    print("Happy Birthday! You are now " + str(i))


print("------------------- CHALLENGE 2 : ITERATOR ----------------------")

#here is a list full of colors...
colors = ['red' , 'violet' , 'cyan' , 'pink' , 'lime' , 'white' , 'yellow', 'black' , 'magenta', 'green', 'orange']

#This is how you can iterate through a list:
for x in colors:
    print("The color is: " + x)

#-->TODO: Declare a list with at least 5 animals. You provide the animals.
animals = ["Squid", "Octopus", "Lion", "Monkey", "Iguana"]

#-->TODO: Print all the animals in the array with a for loop. 
for animal in animals: 
    print(animal)


print("------------------- CHALLENGE 3 : EVEN COUNTDOWN ------------------")


#The line below makes a random number between 0-50 and assigns it to the random variable
random1 = random.randint(0, 50)

#this if/else statement checks if the number is even using the modulo operator (%)
if random1 % 2 == 0:
    print(str(random1) + " is even!")
else:
    print(str(random1) + " is odd!")

#-->TODO: Write a function that counts BACKWARDS from 100 and prints only even numbers
def count_backwards(): 
    for x in range (100, 0, -2): 
        print(str(x))
count_backwards()
#-->TODO: Write a function that counts BACKWARDS from the given random number and prints only odd numbers

def random_odd_backwards(num):
    if(num % 2 == 1): 
        # if num is odd
        for i in range(num, 0, -2):
            print(str(i))
    else: 
        # num would be even
        num += 1
        for i in range(num, 0, -2): 
            print(str(i))

random_number = random.randint(0, 300)
random_odd_backwards(random_number)

print("------------------- CHALLENGE 4 : Finder ------------------")

#This code uses the in operator to see if an element exists in a list. It only has to appear once.
color = input('Type a one word color and see if it is one of my favorite colors! >> ')
if color in colors:
    print("Yes, that color is a fav")
else:
    print("No, that color is not one of my favorites")

#-->TODO Declare a list of any strings you  want: cities, friends, movies, etc.
cities = ["San Jose","Oakland","NYC","Honolulu","Juneau","Beijing","Shanghai","Los Angeles"]


#-->TODO Write function to prompt the user to "Guess" if an element is present in your list. Store their response in a variable. 
#   --> If their guess is in your list, print CONGRATULATIONS!
def guess_city(guess): 
    for i in range(len(cities)): 
        if str(guess) == cities[i]: 
            return "CONGRATULATIONS!"
    return "Sorry, try again."

guessAttempt = input("Guess if a city is in my list!")
#-->TODO Call your function.
print(guess_city(guessAttempt))

print("------------------- CHALLENGE 5 : Nested ------------------")

#this is how you get the length of a word:
big_word = "antidisestablishmentarianism"
print(f"{big_word} has {len(big_word)} letters")

#this is how you can nest for loops, one inside the other! These loop through all the colors, and then through all the characters in the color
for color in colors:
#for all the colors:
    print(color)
    for c in color:
        print(" - " + c) #log each letter. Remember, a string is also an array of characters.


#-->TODO Write a function that prints every letter in a sentence that a user enters.
def print_letters(sentence): 
    words = sentence.split(" ")
    for word in words: 
        for char in word: 
            print(" - " + char)

sentence = input("Input a sentence to see every letter inside it!")
#-->CHALLENGE: Let the user know which word is the shortest one!
def shortest_word(sentence):
    words = sentence.split(" ")
    return min(words, key=len)

print(print_letters(sentence))
print("The shortest word in your sentence is " + str(shortest_word(sentence)))
