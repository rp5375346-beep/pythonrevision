def largest(nums):
    if not nums:
        return None
    largest=nums[0]
    for num in nums:
        if num>largest:
            largest=num
            return largest
        nums=[14,23,12,10]
        print("The largest number is:",largest(nums))