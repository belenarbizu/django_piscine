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
        state = args[1]
        if state in states:
            name = states[state]
            capital = capital_cities[name]
            print(capital)
        else:
            print("Unknown state")


if __name__ == '__main__':
    main()