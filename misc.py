def mex(mylist):
    if len(mylist) == 0:
        return 0
    else:
        for i in range(len(mylist)):
            if i not in mylist:
                return i
    return len(mylist)
