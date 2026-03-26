import sys

def main():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    args = sys.argv
    if len(args) == 2:
        capital = args[1]
        for key, value in capital_cities.items():
            if value == capital:
                state = key
                for key, value in states.items():
                    if value == state:
                        print(key)
                        return
        print("Unknown capital city")


if __name__ == "__main__":
    main()
