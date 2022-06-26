tweets = [
    {"username": "Uncle Chi", "age": 35, "tweets": ["Can i have my class back"], "verify": "true"},
    {"username": "Ade Omoade", "age": 25, "tweets": ["if you can dream it, you can achieve it"], "verify": "false"},
    {"username": "py chan chen", "age": 19, "tweets": ["the you in you is greater  than the you you are"], "verify": "true"},
    {"username": "nutmeg", "age": 40, "tweets": ["together, we can achieve the unthinkable"], "verify": "false"},
    {"username": "megapreneur", "age": 15, "tweets": ["Champions are not born, they are made", "never give up on your dreams"], "verify": "true"},
    {"username": "code father", "age": 20, "tweets": ["hello nigeria", "how we dea"], "verify": "true"},
    {"username": "Uncle bob", "age": 22, "tweets": ["sapa is everywhere", "my money grows like grass"], "verify": "false"},
    {"username": "Aunty bob", "age": 22, "tweets": [], "verify": "false"},
]


print([tweet["username"] for tweet in tweets if tweet["verify"] == "true"])
print([tweet["username"] for tweet in tweets if tweet["age"] < 25 and "true" in tweet["verify"]])
print(sorted([tweet["age"] for tweet in tweets]))
print([tweet["username"] for tweet in tweets if len(tweet["tweets"]) <= 0])

from functools import reduce
from statistics import mean

print(mean(tweet["age"] for tweet in tweets))


avg = reduce(lambda  x, y: x + y, (tweet["age"] for tweet in tweets)) / len(tweets)

print(avg)

user_age =  [tweet["age"] for tweet in tweets]
user_maxi_age = max(user_age)
print(user_maxi_age)

user_mini_age = min(user_age)
print(user_mini_age)

user_age_average = sum(user_age) / len(user_age)
print(f"the average age is {user_age_average: .2f}")


most_tweets = max(tweets, key=lambda user: len(user["tweets"]))
most_tweets2 = max(tweets, key=lambda tweet: len(tweet["tweets"]))["tweets"]
most_tweets2 = max(tweets, key=lambda tweet: len(tweet["tweets"]))["username"]
print(most_tweets)
print(most_tweets2)