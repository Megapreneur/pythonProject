programming_dict = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# Retrieving items from dictionary.
# print(programming_dict["Bug"])

# Adding new items to dictionary.
programming_dict["python"] = "It is a key programming language for data analysis."

# print(programming_dict)

# create an empty dictionary.
empty_dict = {}

for key in programming_dict:
    print(key)
    print(programming_dict[key])


