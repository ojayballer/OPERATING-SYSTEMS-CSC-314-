def first_fit(blockSize,processSize):
    allocated=[0]*len(processSize)
    m=len(blockSize)
    n=len(processSize)
    for i in range(n):#each process(job)
        allocated[i]=-1 #unallocate all the blocks for a job  and set a marker for indication :)

        for j in range(m):#each block
            if blockSize[j]>=processSize[i]:
                allocated[i]=j #update the makrer to show that the block has already been allocated a job
                blockSize[j]-=processSize[i]# the remaianing space left,
                 #to see if we have internal frgamentation and to also know the amount of memory used in this particular block

                break #so we won't allocate the same job more than once,once a job has been allocated... we want to move to allocate the next job

    return allocated,blockSize
    

# Test 
if __name__ == '__main__':
    # Block Sizes 
    blockSize= [100, 500, 200, 300, 600]
    # Process Sizes (The Jobs)
    processSize = [212, 417, 112, 426]

    print("Initial Blocks:", blockSize)
    
   
    allocation_result ,blockSize= first_fit(blockSize,processSize)
    print(f"Blocks Allocated :{allocation_result},space left in each block: {blockSize}") # -1 means a block hasn't been given a job


    
    print("Process No.\tProcess Size\tBlock No.")

    for i in range(len(processSize)):
     if allocation_result[i]!=-1:
      print(f"{i+1}\t\t{processSize[i]}\t\t{allocation_result[i] + 1}")
     else:
        allocation_result[i]="Not Allocated"
        print(f"{i+1}\t\t{processSize[i]}\t\t{allocation_result[i] }")