def var_to_dict():
    d = [
            ('Hendrix'  , '1942'),
            ('Allman'   , '1946'),
            ('King'     , '1925'),
            ('Clapton'  , '1945'),
            ('Johnson'  , '1911')
    ]
    #d.sort()
    print("\n".join(["%s : %s" % (name, year) for year, name in d]))

if __name__ == '__main__':
    var_to_dict()
