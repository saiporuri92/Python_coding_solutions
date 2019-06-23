def dnf(llist,target):
    low = mid = 0
    high = len(llist)-1
    while(mid<=high):
        if llist[mid] == target:
            mid += 1
        elif llist[mid] < target:
            llist[mid],llist[low] = llist[low],llist[mid]
            low += 1
            mid += 1
        else:
            llist[mid],llist[high] = llist[high],llist[mid]
            high -= 1
    print(llist)
dnf([3,5,2,6,8,4,4,6,4,4,3],5)