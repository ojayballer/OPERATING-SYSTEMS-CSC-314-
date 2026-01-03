def priorityScheduler(jobs,priorities):
   combined=sorted(zip(priorities,jobs))
   
   sorted_jobs=[x[1] for x in combined]
   wait_time=[0]*len(sorted_jobs) ;turnaround=[0]*len(sorted_jobs)
   
   for i in range(1,len(sorted_jobs)):
      wait_time[i]=wait_time[i-1]+sorted_jobs[i-1]

   for i in range(len(sorted_jobs)):
      turnaround[i]=wait_time[i]+sorted_jobs[i]

   return turnaround
if __name__ == '__main__':
    jobs = [10, 5, 8]
    priorities = [2, 1, 3] # Lower number = Higher priority
    print(priorityScheduler(jobs, priorities))
