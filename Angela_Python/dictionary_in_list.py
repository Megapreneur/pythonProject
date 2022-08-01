travel_log = [
    {
        "country": "France",
        "cities": ["Paris", "Lille", "Dijon"],
        "visits": 5
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "visits": 7
    },
    {
        "country": "Nigeria",
        "cities": ["Abuja", "Lagos", "Imo"],
        "visits": 28
    },
]
def add_new_country(country_visited, cities_visited, total_visits):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities"] = cities_visited
    new_country["visits"] = total_visits
    travel_log.append(new_country)


add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)

print(travel_log)
