class Solution:
    """
    Naive solution: nested loop.
    O(n^2) time; 
    O(n) space
    
    ** Another way: multiple all elements, divide by nums[i]
    """
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     res = []
    #     for i in range(len(nums)):
    #         runningProd = 1
    #         for j in range(len(nums)):
    #             if i == j:
    #                 continue
    #             runningProd *= nums[j]
    #         res.append(runningProd)

    #     return res

    """
    Near Optimal solution:
    O(n) Time
    O(n) space
    for a given number, the output at that position is the product of prefix product * postfix product
    having 2 arrays: pre and post
   
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_len = len(nums)
        pre, post = [1] * n_len, [1] * n_len
        # input = [1, 2, 3, 4] 
        # pre =   [1, 1, 2, 6]
        # post = [24, 12, 4, 1]
        # output = [24, 12, 8, 6]
        for i in range(n_len):
            if i == 0:
                continue
            pre[i] = nums[i-1] * pre[i-1]
        for i in reversed(range(n_len)):
            if i == n_len - 1:
                continue;
            post[i] = nums[i+1] * post[i+1]

        res = [1] * n_len
        for i in range(n_len):
            res[i] = pre[i] * post[i]

        return res;

    """
    Optimal:  we can go 1st pass, computing all the prefix in the output array
    then go the 2nd pass, mulitplying the prefix with the postfix
    O(1) space (no extra space other than the output array)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate left -> right, compute prefix: output[i] = output[i-1] * nums[i] (use 1 if output out of bound)
        # input = [1, 2, 3, 4] => output = [24, 12, 8, 6]
        # iterate right -> left, computer postfix: output[i] = output[i+1] * 
        n_len = len(nums)
        res = [1] * n_len
        for i in range(n_len):
            if i == 0:
                continue
            res[i] = nums[i-1] * res[i-1]
        # input = [1, 2, 3, 4]
        # res =   [1, 1, 2, 6]
        post = 1
        for i in reversed(range(n_len)):
            if i == n_len - 1:
                continue
            post *= nums[i+1]
            res[i] *= post
        
        return res

            

            
        

        