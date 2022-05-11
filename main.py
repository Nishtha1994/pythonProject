
def compareStrings(a,b):

    a = a.split('.')
    b = b.split('.')

    while a or b:
        if a:
            aVal=int(a.pop(0))
        else:
            aVal=0
        if b:
            bVal=int(b.pop())
        else:
            bVal=0
        if aVal > bVal:
            return 1
        elif bVal > aVal:
            return -1
    return 0


if __name__ == '__main__':
    print(compareStrings("1.2.9.9.9.9.9.9.9.9.9.10.100", "1.101"))
    print(compareStrings("134.2.9.919.9.9.9.9.9.9.9.10.100", "1.101"))
    print(compareStrings("1.01", "1.001"))
    print(compareStrings( "12.09","12.2"))

