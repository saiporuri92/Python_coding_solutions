#sorting bits of 1s and 0s in linear time using read and write pointers
#it is a form of fast and slow pointers.
def sortme(li):
    read = 0
    write = 0
    while(read<len(li)):
        if li[read] == 1:
            read += 1
        else:
            li[read],li[write] = li[write],li[read]
            read += 1
            write += 1
    return li
print(sortme([0, 1, 1, 0, 1, 1, 1, 0]))