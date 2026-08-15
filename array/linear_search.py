def linearSearch(nums, target):
        output=-1
        for i in range(0,len(nums)):
            if nums[i]==target:
                output =i
                return output
        return output

a=[2,1,2]
print(linearSearch(a,3))