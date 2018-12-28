#!/Users/narajaon/.brew/bin/python3

import sys

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

def get_state(name):
    for c_key in capital_cities:
        if capital_cities[c_key] == name:
            for s_key in states:
                if states[s_key] == c_key:
                    return "{} is the capital of {}".format(name, s_key)
    return None

def get_capital(name):
    try: 
        return "{}'s capital is {}".format(name, capital_cities[states[name]])
    except KeyError: 
        return None

def split_arg(input):
    return input.split(',')

def check_input(input):
    capital = get_capital(input)
    if capital:
        return capital
    state = get_state(input)
    if state:
        return state
    return '{} is neither a capital city nor a state'.format(input)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        formated = split_arg(sys.argv[1])
        for val in formated:
            print(check_input(val.strip()))
