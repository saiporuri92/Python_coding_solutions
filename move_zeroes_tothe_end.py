#using a read and write pointer
def move(llist):
    read = write = len(llist)-1
    while(read>=0):
        if llist[read] != 0:
            read -= 1
        else:
            llist[read],llist[write] = llist[write],llist[read]
            read -= 1
            write -= 1
    print(llist)
move([2,3,0,3,0,1,0])