def word_weight(word, n):
  """
  Calculates the final weight of a word after applying the given rules n times.

  Args:
    word: The word to process.
    n: The number of times to apply the rules.

  Returns:
    The final weight of the word after n iterations.
  """

  # Create a dictionary mapping characters to their corresponding weights (1-based).
  char_to_weight = {chr(i): i - 96 for i in range(97, 123)}

  # Convert the word to a list of weights.
  word_weights = [char_to_weight[c] for c in word]

  # Apply the rules n times.
  for _ in range(n):
    # Sum the digits of the current weight.
    current_sum = sum(word_weights)

    # Update the word_weights list with the new digits.
    word_weights = [int(d) for d in str(current_sum)]

  # Return the final weight.
  return sum(word_weights)

# Example usage
word = "turing"
n = 2
final_weight = word_weight(word, n)

print(f"Word: {word}, Iterations: {n}")
print(f"Final Weight: {final_weight}")
