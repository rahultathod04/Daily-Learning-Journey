def First(nums: list[int], target: int) -> int:
    l, r = 0 , len(nums)-1
    first = -1
    while(l<=r):
        mid = l+(r-l)//2
        if nums[mid] == target:
            first = mid
            r = mid-1
        elif(nums[mid]<target):
            l = mid+1
        else:
            r = mid-1
    return first


def Last(nums: list[int], target: int) -> int:
    l, r = 0 , len(nums)-1
    last = -1
    while(l<=r):
        mid = l+(r-l)//2
        if nums[mid] == target:
            last = mid
            l = mid+1
        elif(nums[mid]<target):
            l = mid+1
        else:
            r = mid-1
    return last


if __name__ == '__main__':
    nums = [1,2,3,4,4,4,4,4,4,5,6,7,8,8,9]
    target = 4
    first = First(nums, target)
    last = Last(nums, target)
    print(first, last)