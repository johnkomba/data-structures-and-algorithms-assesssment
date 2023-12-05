from is_balanced import is_balanced
from remove_duplicates import remove_duplicates
from word_frequency import word_frequency

# Question 1: is_balanced
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

# Question 2: remove_duplicates
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

# Question 3: word_frequency
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
