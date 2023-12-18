#10. Write a Python program to reverse the order of words in a given sentence.
#input_sentence = “Hello, World! Welcome to Python programming.”
#Output after reverse = “programming. Python to Welcome World! Hello,”


def reverse_sentence(input_word):
    words = input_word.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_word = input()
word = reverse_sentence(input_word)
print(word)
