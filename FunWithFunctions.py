def odd_even( start, end ):
    for i in range( start, end+1 ):
        if i % 2 == 0:
            print "Number is", i, ". This is an even number."
        else:
            print "Number is", i, ". This is an odd number."
odd_even( 1, 10 )

print "-"
print "-"
print "-"

def multiply( listName, multiplier ):
    for i in range( len( listName ) ):
        listName[i] *= multiplier
    print listName
    return listName
someList = [2,4,10,16]
multiply( someList, 5 )

print "----- end of multiply ------"
print "-"
print "-"
print "-"

def layered_multiples( arg ):
    newList = []
    multipliers = multiply( arg[0], arg[1])
    for i in range( len( multipliers ) ):
        newInnerList = []
        for j in range( multipliers[i] ):
            newInnerList.append(1)
        newList.append(newInnerList)
    print newList

    
arg = ([2,4,5],3)
layered_multiples( arg )

print "------"