def Capaciyt_of_ship(weights: list[int], days: int) -> int:
    if days == 1:
        return sum(weights)
    if days == len(weights):
        return max(weights)

    l = max(weights)
    r = sum(weights)

    ans = r

    def can_ship(capacity: int):
        cur_day = 1
        cur_w = 0
        for w in weights:
            if(cur_w + w > capacity):
                cur_day +=1
                cur_w = w
            else:
                cur_w +=w
        return cur_day<=days


    while l<=r:
        mid = l+(r-l)//2

        if(can_ship(mid)):
            ans = mid
            r = mid-1
        else:
            l = mid+1
    return ans

if __name__ == '__main__':
    weights = [3,2,2.4,1,4]
    days = 3

    capacity = Capaciyt_of_ship(weights, days)
    print(capacity)