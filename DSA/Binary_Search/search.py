def Search(nums: list[int], target: int ) -> int:
    l = 0
    r = len(nums)-1

    while l<=r:
        mid = l+(r-l)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l = mid+1
        else:
            r = mid-1
    return -1
if __name__ == '__main__':
    elements = [1,2,3,45,66,123,675]
    target = 66

    index = Search(elements, target)
    print(index)