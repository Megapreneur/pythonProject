# word = "goal"
# word2 = "F" + word[1:]
# print(word2)
# print(word.upper())
# print(word2.lower())
# print(len(word))
# print(len(word2))
# name = "Ademola Megbabi      "
# name1 = "      Ademola Megbabi"
# name2 = "                    Ademola Megbabi           "
# print(name.rstrip())
# print(name1.lstrip())
# print(name2.strip())
#
# response = input("What should i shout? ")
# shouted_response = response.upper()
# print("We, if you insist...", shouted_response)

user_password = input("What is your password? ")
if(len(user_password) > 0):
    first_letter = user_password[0]
    print("The first letter you entered was: " + first_letter.upper())
else:
    print("Nothing was typed")


