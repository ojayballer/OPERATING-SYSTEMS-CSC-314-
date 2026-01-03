def SJN(jobs):
    jobs.sort()
    wait_time=[0]*len(jobs); total_wait=0#counter
    turnaround=[0]*len(jobs)
    for i in range(1,len(jobs)): #the wait time of the first job is always 0
        #current wait time=previous wait time +previous job's length
        wait_time[i]=wait_time[i-1]+jobs[i-1]
    for i in range(len(jobs)):   
        #to store the total wait time
        turnaround[i]=wait_time[i]+jobs[i]
    return turnaround

if __name__ == '__main__':
    jobs = [6, 8, 7, 3]
    print(SJN(jobs))
