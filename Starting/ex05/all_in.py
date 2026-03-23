import sys


def search_capital_states(item, states, capital_cities):
    for key, value in capital_cities.items():
        if item == value.lower():
            state = key
            capital = value
            for key, value in states.items():
                if state == value:
                    return capital, key
    for key, value in states.items():
        if item == key.lower():
            state = value
            state_name = key
            for key, value in capital_cities.items():
                if state == key:
                    return value, state_name
    return None, None


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
        content = args[1].split(',')
        content = [item.strip() for item in content]
        # add only existing items
        content = [item for item in content if item]
        for item in content:
            capital, state = search_capital_states(item.lower(), states, capital_cities)
            if capital and state:
                print(f"{capital} is the capital of {state}")
            else:
                print(f"{item} is neither a capital city nor a state")


if __name__ == "__main__":
    main()