import sys

def find_capital(argv):
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
    val = states.get(argv[1], "Unknown state")
    print(capital_cities.get(val, "Unknown state"))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    find_capital(sys.argv)
