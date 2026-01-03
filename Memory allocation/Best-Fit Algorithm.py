def best_fit(blockSize,processSize):
    m=len(blockSize);n=len(processSize)
    allocated=[0]*n
    for i in range(n):
        best=-1
        for j in range(m):
            if blockSize[j]>=processSize[i]:

                if best==-1 or blockSize[j]<blockSize[best]:
                    best=j
        if best != -1:
            allocated[i]=best
            blockSize[best]=blockSize[best]-processSize[i]

    return allocated,blockSize

if __name__ == '__main__':
    # Block Sizes 
    blockSize= [100, 500, 200, 300, 600]
    # Process Sizes (The Jobs)
    processSize = [212, 417, 112, 426]

    print("Initial Blocks:", blockSize)
    
   
    allocation_result ,blockSize= best_fit(blockSize,processSize)
    print(f"Blocks Allocated :{allocation_result},space left in each block: {blockSize}") # -1 means a block hasn't been given a job
