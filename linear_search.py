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

def locate_card(cards,query):
    position = 0
    if position == len(cards):
        return -1
    else:
        for card in range(len(cards)):
            if cards[card] == query:
                return position
            position += 1
    return -1


cards = [13,11,7,12,7,4,3,1,0]
query = 7
output = 3
result = locate_card(cards,query)
print(result)

for test_data in test_data:
    result1 = locate_card(**test_data['input'])
    print(result1 == test_data['output'])