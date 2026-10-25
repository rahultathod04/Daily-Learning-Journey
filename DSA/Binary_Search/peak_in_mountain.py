def Peak(nums: list[int])-> int:
    l = 0
    r =len(nums)-1

    while l<=r:
        mid = l+(r-l)//2

        if(nums[mid]<nums[mid+1]):
            l = mid+1
        else:
            r = mid-1
    return nums[l]

if __name__ == '__main__':
    nums = [1,2,3,5,7,90,8,6,4]
    peak = Peak(nums)
    print(peak)
