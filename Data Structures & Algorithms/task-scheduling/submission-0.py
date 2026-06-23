class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        2 heaps: minHeap to store tasks on cooldown, maxHeap to store available tasks
        minHeap[(availableAtCycle, remainingTaskCnt, task)]
        maxHeap[(remainingTaskCnt, task)]

        cycle = 1
        while minHeap or maxHeap:
            keep popping minHeap while availableAtCycle == cycle off of minHeap, add them to maxHeap

            if maxHeap:
                task = popMaxheap
                run task
                remainingTaskCnt--
                push to minHeap with availableAtCycle = n + cycle + 1, 
            
            else:    
                idle
            cycle++
        return cycle
        """

        minHeap = []
        freq = defaultdict(int)
        for task in tasks:
            freq[task] -= 1
        maxHeap = [(taskCnt, task) for (task, taskCnt) in freq.items()]
        heapq.heapify(maxHeap)

        cycle = 0
        while minHeap or maxHeap:
            while minHeap and minHeap[0][0] == cycle:
                availableAtCycle, taskCnt, task = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (taskCnt, task))

            if maxHeap:
                taskCnt, task = heapq.heappop(maxHeap)
                taskCnt += 1
                # run task
                if taskCnt < 0:
                    heapq.heappush(minHeap, (cycle+n+1, taskCnt, task))
            
            cycle += 1
        
        return cycle
