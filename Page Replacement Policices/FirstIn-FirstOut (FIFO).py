def FIFO(pages,capacity):
    memory=[]
    n=len(pages)
    faults=0

    for  i in range(n):
        if pages[i] not in memory: #if page is in memory,we skip this iteration and load the next page(job) because we don't want to add duplicates to memory
            faults+=1
            if len(memory) == capacity:#pages 
               memory.pop(0) #First-In -First-Out
            memory.append(pages[i])
    
    return memory,faults 

if __name__ == '__main__':
    pages = [1, 3, 0, 3, 5, 6, 3]
    capacity = 3
    print(FIFO(pages, capacity))