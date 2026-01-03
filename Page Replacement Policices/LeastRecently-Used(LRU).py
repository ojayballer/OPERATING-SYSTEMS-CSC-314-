def LRU(pages,capacity):
    memory=[]
    faults=0

    for i in range(len(pages)):
        if pages[i] not in memory:
            faults+=1
            if len(memory)==capacity:# if memory is full..
                memory.pop(0) #Index-0 is always the Least-Recently-Used     
            memory.append(pages[i])

        else:
            memory.pop(memory.index(pages[i])) #.pop doesn't take values only indexes
            memory.append(pages[i]) # take the page to the most recent index

    return memory,faults

if __name__ == '__main__':
    pages = [1, 2, 3, 2, 4, 1, 5]
    capacity = 3
    print(LRU(pages, capacity))