import sys

def all_in(argv):
    i = 0
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
    if argv.lower() != argv or argv.upper() != argv:
        argv = argv.capitalize()
        for valeur in capital_cities.values():
            if valeur == argv:
                val = list(capital_cities.keys())[list(capital_cities.values()).index(argv)]
                state_name = list(states.keys())[list(states.values()).index(val)]
                print(argv, "is the capital of", state_name)
                i = 1
        if i == 0:
            for cle in states.keys():
                if cle == argv:
                    val = states.get(argv)
                    capital_name = capital_cities.get(val)
                    print(capital_name, "is the capital of", argv)
                    i = 2
        if i == 0:
            print(argv, "is neither a capital or a state")

def splitter(argv):
    content = argv[1].split(",")
    for elem in content:
        all_in(elem.strip())

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    splitter(sys.argv)
