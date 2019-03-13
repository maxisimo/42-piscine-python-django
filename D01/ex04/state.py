import sys

def find_state(argv):
    states = {
            "Oregon"    : "OR",
            "Alabama"   : "AL",
            "New Jersey": "NJ",
            "Colorado"  : "CL",
    }
    capital_cities = {
            "OR"    : "Salem",
            "AL"    : "Montgomery",
            "NJ"    : "Trenton",
            "CL"    : "Denver",
    }
    for valeur in capital_cities.values():
        if valeur == argv[1]:
            val = list(capital_cities.keys())[list(capital_cities.values()).index(argv[1])]
            print(list(states.keys())[list(states.values()).index(val)])
            sys.exit(1)
    print("Unknown capital city")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    find_state(sys.argv)
