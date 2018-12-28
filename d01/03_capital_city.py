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

def get_capital(name):
    try: 
        return capital_cities[states[name]]
    except KeyError: 
        return 'Unknown state'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(get_capital(sys.argv[1]))
