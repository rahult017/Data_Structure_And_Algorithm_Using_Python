def locate_card(cards,query):
    low, high = 0, len(cards) - 1
    
    # while low <= high:
    for _ in range(len(cards)):
        mid = (low + high) // 2
        result = test_locate(cards,query,mid)
        if result == "Found":
            return mid
        elif result == "Left":
            high = mid - 1 
        elif result == "Right":
            low = mid+1

        # mid_number = cards[mid]
        
        # #print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        # if mid_number == query:
        #     return mid
        # elif mid_number < query:
        #     high = mid - 1  
        # elif mid_number > query:
        #     low = mid + 1
    
    return -1

def test_locate(cards,query,mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid -1 >= 0 and cards[mid-1] == query:
            return "Left"
        else:
            return "Found"
    elif mid_number < query:
        return "Left"
    else:
        return "Right"
    

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3
# result = locate_card(cards,query)
# print(result)
test_data =[{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
  'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
   'query': 6},
  'output': 2}]

# for test_data in test_data:
#     result1 = locate_card(**test_data['input'])
#     print(result1,test_data['output'])

#o(logn)
#o(1)
    

# Generic way 
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

def rewrite_locate_card(cards,query):
    def condition(mid):
        mid_number = cards[mid]
        if mid_number == query:
            if mid -1 >= 0 and cards[mid-1] == query:
                return "Left"
            else:
                return "Found"
        elif mid_number < query:
            return "Left"
        else:
            return "Right"
    return binary_search(0,len(cards)-1,condition)
print(rewrite_locate_card(cards,query))