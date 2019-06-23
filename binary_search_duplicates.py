def dups(llist,target):
    low = 0
    high = len(llist)
    while(low<high):
        mid = low + (high-low)//2
        if llist[mid] > target or (llist[mid] == target and llist[mid-1]==target):
            high = mid - 1
        elif llist[mid] < target:
            low = mid + 1
        else:
            print(mid)
            return
dups([1,3,4,6,6,6,7],6)