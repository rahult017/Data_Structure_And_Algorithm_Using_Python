def binary_search(low,high,condition):
    while low <= high:
        mid = (low + high) //2
        result = condition(mid)
        if result == "Found":
            return mid
        elif result == "Left":
            high = mid - 1
        else:
            low = mid + 1
    return -1

def first_position(num,target):
    def condition(mid):
        if num[mid] == target:
            if mid > 0 and num[mid-1] == target:
                return "Left"
            return "Found"
        elif num[mid] < target:
            return "Right"
        else:
            return "Left"       
    return binary_search(0,len(num)-1,condition)


def last_position(num,target):
    def condition(mid):
        if num[mid] == target:
            if mid < len(num)-1 and num[mid+1] == target:
                return "Right"
            return "Found"
        elif num[mid] < target:
            return "Right"
        else:
            return "Left"
    return binary_search(0,len(num)-1,condition)

def first_and_lsat_position(num,target):
    return first_position(num,target),last_position(num,target)

nums =[5,7,7,8,8,10] 
target = 8
print(first_and_lsat_position(nums,target))