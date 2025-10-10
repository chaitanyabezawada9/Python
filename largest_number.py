def getLargestNum(nums):
    largestNum = nums[0];
    for num in nums:
        if largestNum < num:
            largestNum = num;
    print(largestNum)
    return largestNum
    
getLargestNum([3,1,21])


#output: 21
