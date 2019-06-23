def record(llist,target):
    closest = None
    low = 0
    high = len(llist)
    while(low <= high):
        mid = low + (high-low) // 2
        