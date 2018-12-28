#!/Users/narajaon/.brew/bin/python3

d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
        }

def cmp_to_key(mycmp):
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

if __name__ == '__main__':
    tuple_array = []

    for key in d:
        tuple_array.append((key, d[key]))

    def custom_sort(first, sec):
        if first[1] == sec[1]:
            return 1 if first[0] >= sec[0] else -1
        return 1 if first[1] > sec[1] else -1

    new_array = sorted(tuple_array, key=cmp_to_key(custom_sort))

    for elem in new_array:
        """printing the date anyway"""
        print('{} : {}'.format(elem[1], elem[0]))
