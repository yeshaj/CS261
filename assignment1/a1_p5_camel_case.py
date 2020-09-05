# Course: CS 261 - Data Structures
# Student Name: Yesha Jhala
# Assignment: Assignment 1 Part 5 Camel Case
# Description: Will write out three functions which, working together, will convert a given input string to a “camelcase” string using specific rules described below.
# Input string will consist of any printableASCII characters (english letters, digits, spaces, underscores, some special characters).


def length(input_string: str) -> int:
    """
    return count of letters in the string
    """
    count = 0
    for _ in input_string:
        count += 1
    return count


def input_cleanup(input_string: str) -> str:
    """
    string of leading/trailing non characters, then converts characters to lower case, converting any non characters into underscores
    """

    output = ""
    length_output = 0
    for c in input_string:
        # check if it is a character
        if not is_char(c):
            if length_output != 0:
                if is_char(output[length_output - 1]):
                    output += "_"
                    length_output += 1
        # convert to lower case if it is upper case character and add to length
        else:
            output += to_lower(c)
            length_output += 1

    if length_output != 0:
        while not is_char(output[length_output - 1]):
            output = output[:-1]
            length_output -= 1
    return output


def is_clean_string(input_string: str) -> bool:
    """
    will check if the string input is clean
    """
    return input_string == input_cleanup(input_string)


def camel_case(input_string: str, func_is_clean, func_cleanup):
    """
    takes non camel case to turn into camel case
    :param input_string: string that has to be converted
    :param func_is_clean: if the string is clean will return true
    :param func_cleanup: function that cleans up string
    """
    # sanitize input string
    clean_input = func_cleanup(input_string)     # DO NOT DELETE / CHANGE

    # check if input string is ready for camelCase conversion

    if not func_is_clean(clean_input):           # DO NOT DELETE / CHANGE
        return None                              # DO NOT DELETE / CHANGE

    # check that input string has at least two words in it (has at least 1 separator)
    separator_count = 0
    for i in clean_input:
        if not is_char(i):
            separator_count += 1

    # return None if it does not
    if separator_count < 1:
        return None

    # convert clean input string into camelCase
    separator_index = 0
    output = ""
    for i in range(length(clean_input)):
        if not is_char(clean_input[i]):
            if separator_index != 0:
                new_word = capitalize_str(clean_input[separator_index + 1: i])
                separator_index = i
                output += new_word
            else:
                output += clean_input[:i]
                separator_index = i
    output += capitalize_str(clean_input[separator_index + 1:])
    return output

def is_char(c: str) -> bool:
    """checks to make sure that it's in the alphabet"""
    return 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90


def to_lower(c: str) -> str:
    """ converts a character to lowercase if uppercase or returns original"""
    if 65 <= ord(c) <= 90:
        return chr(ord(c) + 32)
    return c


def to_upper(c: str) -> str:
    """will convert all to uppercase and return
    if already uppercase, then returns original """
    if 97 <= ord(c) <= 122:
        return chr(ord(c) - 32)
    return c

def capitalize_str(c: str) -> str:
    """ capitalizing the string and returning it"""
    return to_upper(c[0]) + c[1:]




# BASIC TESTING
#if __name__ == "__main__":
#    if __name__ == "__main__":
#        test_set = ("_random_ _word_provided",
#                    "@$ptr*4con_", " ran  dom  word",
#                    "example    word   ", "ANOTHER_Word",
#                    "__", "_ _ _", "    ", "435%7_$$", "random")

        # example 1
#        for test_string in test_set:
#            result = input_cleanup(test_string)
#            print(length(result), result)
#        print()

        # example 2
#        for test_string in test_set:
#            result = input_cleanup(test_string)
#            print(is_clean_string(test_string), is_clean_string(result))
#        print()

        # example 3
#        for test_string in test_set:
#            result = camel_case(test_string, is_clean_string, input_cleanup)
#            print("'" + test_string + "'", "-->", result)