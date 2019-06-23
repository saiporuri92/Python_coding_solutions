def target(llist,target):
    seen = set()
    for i in llist:
        if target - i in seen:
            return [target-i,i]
        else:
            seen.add(i)

print(target([6,3,5,2,1,7],4))
