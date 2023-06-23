# Dictionary in list

travel_log = [
    {
        "country": "Egypt",
        "visits": 12,
        "cities":["France", "Dubia", "canada"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities":["Berlin", "Mexico", "Argentina"],
    }
]
def add_new_country(country_visited, times_visited, cities_visited):
    country ={}
    country["country"] = country_visited
    country["visits"] = times_visited
    country["cities"] = cities_visited
    travel_log.append(country)
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Secret auction

Deal = {}
playing = True

def auction(Dealer):
    highest = 0
    win_name = ""
    for Dealsder in Dealer:
        Deals_amount = Dealer[Dealsder]
        if Deals_amount > highest:
            highest = Deals_amount
            win_name = Dealsder
            print(f"{win_name} wins with a Deals of {highest}")

while playing:
    name = input("Please enter your name: ").lower()
    Deals = int(input("Enter your Deals: $"))
    Deal[name] = Deals
    

    print("insert 'No' or 'Yes' for the Next step".title())
    Next_round = input("Any other Dealerr: ")
    if Next_round == "No":
        playing = False
        auction(Deal)