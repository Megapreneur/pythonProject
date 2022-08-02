# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Hungary": "Budapest",
    "Nigeria": "Abuja",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Nigeria": ["Abuja", "Lagos", "Kebbi"],
}

# Nesting Dictionary in a Dictionary

travel_diary = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 5},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 7},
    "Nigeria": {"cities_visited": ["Abuja", "Lagos", "Imo"], "total_visits": 28},
}

# Nesting a dictionary in a List.

travel_diary2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 5
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 7
    },
    {
        "country": "Nigeria",
        "cities_visited": ["Abuja", "Lagos", "Imo"],
        "total_visits": 28
    },
]

#
# number = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24}
#
# result = [x for x in number if x % 2 == 0 and x % 3 == 0]
# print(result)
