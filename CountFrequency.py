'''Write a program that takes a string as input,and counts the frequency of each word in
the string, there might be repeated characters in the string.
Your task is to find the highest frequency and returns the length
of the highest-frequency word.'''

#######################################

from collections import Counter
def get_highest_frequency_word_length(input_string):
    words = input_string.split()
    word_frequency = Counter(words)
    highest_frequency = max(word_frequency.values())
    highest_frequency_word_length = max(len(word) for word, freq in word_frequency.items() if freq == highest_frequency)
    return highest_frequency_word_length
def main():
    input_string = input("Enter a string: ")
    result = get_highest_frequency_word_length(input_string)
    print("Length of the highest-frequency word:", result)
if __name__ == "__main__":
    main()
