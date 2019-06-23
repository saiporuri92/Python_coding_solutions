def twosum(llist,t):
    i = 0
    j = len(llist)-1
    while(i<j):
        if llist[i] + llist[j] == t:
            print([llist[i],llist[j]])
            return
        if llist[i] + llist[j] < t:
            i += 1
        else:
            j -= 1
    print(None)
twosum([1,2,3,5,6,7],9)