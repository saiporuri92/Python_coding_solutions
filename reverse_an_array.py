def rev(llist):
    i = 0
    j = len(llist) - 1
    while(i<j):
        llist[i],llist[j] = llist[j],llist[i]
        i+=1
        j-=1
    print(llist)
rev([1,2,3,4,5,6])