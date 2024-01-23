trovel_log = [
    {
        "coutnry": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Humburg", "Stuttgard"]
    }
]

def add_new_country(country, num_visiteds, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = num_visiteds
    new_country["cities"] = cities
    trovel_log.append(new_country)

add_new_country("Russia", 2, ["Mascow", "Saint Petrzbork"])
print(trovel_log)