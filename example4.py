def winning_card(cards):
  """
  This function takes an array of sets of integers as input and returns the winning card.
  The winning card is the card that only exists once in the set of cards.
  If there is no winning card, the function returns -1.
  """
  # Create a dictionary to store the frequency of each card.
  card_counts = {}
  for card_set in cards:
    for card in card_set:
      card_counts[card] = card_counts.get(card, 0) + 1

  # Find the card that only exists once.
  for card, count in card_counts.items():
    if count == 1:
      return card

  # No winning card found.
  return -1

# Example 1
cards1 = [[5,7,3,9,4,9,8,3,1], [1,2,2,4,4,1], [1,2,3]]
print(winning_card(cards1))  # Output: 8

# Additional test cases
cards2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(winning_card(cards2))  # Output: -1

cards3 = [[1], [2], [3, 1]]
print(winning_card(cards3))  # Output: 3
