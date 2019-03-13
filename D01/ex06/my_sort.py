from operator import itemgetter

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
    d.sort(key=itemgetter(1,0))
    print("\n".join(["%s" % (name) for name, year in d]))

if __name__ == '__main__':
    my_sort()
