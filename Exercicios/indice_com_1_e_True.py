def indice(item, lis):
        '''
        (object,list) -> int ou None
        Receives an 'item' object and a 'list' list and returns the
        index of the position in which item occurs in the list.
        If item does not occur in the list, the function returns None
        '''
        for i,v in enumerate(lis):
            if v == item and type(v) == type(item):
                return i
        return None
        
lista  = [1,"hi", 3.14, 7, True]

# test 1
if indice("hi",lista) == 1:
    print("Passed the first test! :-)")
else:
    print("Not passed the first test! :-(")

# test 2
if indice(True,lista) == 4:
    print("Passed the second test! :-)")
else:
    print("Not passed the second test! :-(")

# test 3
if indice(False,lista) == None:
    print("Passed the third test! :-)")
else:
    print("Not passed the third test! :-(")
