def my_sort():
    d = [
            ('Hendrix'  , '1942'),
            ('Allman'   , '1946'),
            ('King'     , '1925'),
            ('Clapton'  , '1945'),
            ('Johnson'  , '1911'),
            ('Berry'    , '1926'),
            ('Vaughan'  , '1954'),
            ('Cooder'   , '1947'),
            ('Page'     , '1944'),
            ('Richards' , '1943'),
            ('Hammett'  , '1962'),
            ('Cobain'   , '1967'),
            ('Garcia'   , '1942'),
            ('White'    , '1975')
    ]
    items = d.items()
    comp = lambda a,b : cmp(a[1],b[1])
    print(sorted(items, comp, reverse=False))
    #print("\n".join(["%s : %s" % (name, year) for year, name in d]))

if __name__ == '__main__':
    my_sort()
