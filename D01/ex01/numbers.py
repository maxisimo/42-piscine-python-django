def numbers() :
    with open("nombres", "r") as my_file:
        content = my_file.read().split(",")
    for elem in content:
        print(elem.strip())

if __name__ == '__main__' :
    numbers()
