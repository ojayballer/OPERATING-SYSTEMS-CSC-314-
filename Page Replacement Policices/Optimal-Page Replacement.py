def OPR(pages,capacity):
    memory=[]
    faults=0
    for i in range(len(pages)):
        if pages[i] not in memory:
            faults+=1
            if len(memory)==capacity:
                list_ahead=pages[i+1:]
                kill=-1 #to store pages we decide to remove
                farthest=-1 #to track the page that is farthest
                for page in memory:
                    #case1
                    if page not in list_ahead:
                        kill=page
                        break
                    #case2
                    else:
                        nxt=list_ahead.index(page)
                        if nxt>farthest:
                            farthest=next
                            kill=page
                memory.remove(kill)
            memory.append(pages[i])
    return memory,faults

if __name__ == '__main__':
    pages = [1, 2, 3, 2, 4, 1, 5]
    capacity = 3
    print(OPR(pages, capacity))