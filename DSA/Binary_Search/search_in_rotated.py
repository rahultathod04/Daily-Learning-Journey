def Rotated_search(nums: list[int], target: int ) -> int:
    left = 0
    right = len(nums)-1

    while left<=right:
        mid = left+(right-left)//2
        if(nums[mid]==target):
            return mid

        if(nums[mid]>=target):
            if(nums[left]<=target<nums[mid]):
                right = mid-1
            else:
                left = mid+1
        else:
            if(nums[mid]<target<=nums[right]):
                left = mid+1
            else:
                right = mid-1
    return -1

if __name__ == '__main__':
    nums = [4,5,6,7,8,1,2,3]
    t1 = 2
    print(Rotated_search(nums, t1))

    t2 = 5
    print(Rotated_search(nums, t2))

