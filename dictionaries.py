#############################################################################
 #                                                                  
 #  Team Edge dictionaries: Dictionaries CHALLENGES 
 # 
 #  For this activity, you will be building a dictionary and with properties
 #  and methods. You will access the properties, set new values, and use
 #  the methods to change your dictionary state. What dictionary? Ask your coach.
 # 
 #  1. DEFINE: Make a dictionary and set its properties, printing changes in between.
 #  2. MODIFY: Add 2 new properties and assing values. Change existing values,
 #     including adding or updating values inside lists
 #  3. METHODS: Now its time to make some methods tha can make a change
 #     to your values, like a boolean, or they can print something about
 #     the dictionary. Nothing fancy, unless you fancy it.
 #  4. LITERALLY: Use string literals to put it all together in one statement.
 # 
 # #########################################################################/

print("------------------- CHALLENGE 1 : DEFINE    -------------------")

#Below is a simple example of a dictionary implementaion. 
#-->TODO: Add at least 3 comments to the dictionary below to demonstrate you understand its usage

dictionary = {
    "name": "box",
    "is_empty": True
}
#working with the dictionary:
dictionary["length"] = 12
dictionary["width"] = 8
dictionary["contents"] = ["thing 1", "thing 2", "thing 3"]
print(f"{dictionary['name']} is {dictionary['length']} {dictionary['width']}")
dictionary["contents"].append("thing 4")
print(f"{dictionary['name']} has {dictionary['contents']}")
print(dictionary)

 

#-->TODO: Declare a new dictionary and set at least 4 properties to it including: string, boolean, number, list

##################################  MY dictionary ########################### #/

new_dict = {
    "name": "Johnny",
    "adult": False, 
    "age": 16,
    "hobbies": ["tennis", "reading", "coding", "eating"]
}





########################################################################## #/



print("------------------- CHALLENGE 2 : MODIFY   -------------------")

#-->TODO: Print your dictionary you created above
print(new_dict)

#-->TODO: Update the dictionary you just created  by adding new properties and values, including list elements, in this section.
# new_dict["name"] = "random"
new_dict["favorite subject"] = "mathematics" 
new_dict["favorite food"] = "noodles"
new_dict["hobbies"].append("talking to people")

#-->TODO: Print your dictionary again and observe changes
print(new_dict)

print("------------------- CHALLENGE 3 : METHODS   -------------------")


#-->TODO: Make a method that will update your dictionary value. It should take in a dictionary and return it modified.
def update_dict(dictionary, key, value): 
    dictionary[key] = value
    return dictionary

#-->TODO: Call the method.
# print(update_dict(new_dict, ))


print("------------------- CHALLENGE 4 : LITERALLY   -------------------")

#-->TODO: Put it all together using a string literal to tell the story of your dictionary!
# My table: 
def return_elements(list):
    ret_string = ""
    for l in list: 
        ret_string += str(l) + ", "
        if l == list[len(list)-1]: # if it's the last element, we don't want to add another space and comma
            ret_string += str(l) + ""
    return ret_string

print("My name is " + str(new_dict["name"]) + ".\n" 
+ "Am I an adult? " + str(new_dict["adult"]) + ".\n" 
+ "My age is " + str(new_dict["age"]) + ".\n"
+ "My hobbies are " + return_elements(new_dict["hobbies"]) + ".\n" 
+ "Has this dictionary been modified? Yes! " + str(update_dict(new_dict, "age", 18)) + "."
)

# Brandon's table: 
# def stringLiteral(dict): 
#     stringLit = ""
#     for key,value in dict.items(): 
#         stringLit = str(key) + ","
#         stringLit = str(value) + ","
#     return stringLit

# print(stringLiteral(new_dict))