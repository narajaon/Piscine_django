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
        "CO": "Denver",
        "S": "D"
        }

def get_state(name):
    for c_key in capital_cities:
        if capital_cities[c_key] == name:
            for s_key in states:
                if states[s_key] == c_key:
                    return s_key
    return 'Unknow capital capial city'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(get_state(sys.argv[1]))
