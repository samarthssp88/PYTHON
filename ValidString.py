'''Write a program that takes a string as input,and determines if all characters of the string
appear the same number of times. If so,return "YES".
Otherwise, check if removing just one character at any index in the string
will make all characters appear the same number of times. If so, return "YES".
Otherwise, return "NO".
Example:
Input 1 = “abc”. This is a valid string because
frequencies are {“a”: 1,
“b”: 1,
“c”: 1}
Output 1- YES
Input 2 = “abcc”. This string is not valid as we
can remove only 1 occurrence of “c”. That
leaves character frequencies of
{ “a”: 1,
“b”: 1 ,
“c”: 2 }
Output 2 – NO'''
############################

from collections import Counter

def is_valid_string(s):
    char_freq = Counter(s)
    freq_values = set(char_freq.values())
    if len(freq_values) == 1:
        return "YES"
    for char in char_freq:
        char_freq_removed = char_freq.copy()
        char_freq_removed[char] -= 1
        freq_values_removed = set(char_freq_removed.values())
        if len(freq_values_removed) == 1:
            return "YES"
    return "NO"
def main():
    input_string = input("Enter a string: ")
    result = is_valid_string(input_string)
    print("Output:", result)

if __name__ == "__main__":
    main()
