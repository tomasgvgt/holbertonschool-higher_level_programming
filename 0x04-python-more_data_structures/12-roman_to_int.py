#!/usr/bin/python3
def roman_to_int(roman_string):
    # Converts a roman numeral into an integer
    r_sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    if not roman_string or type(roman_string) is not str:
        return None
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1:
            if r_sym[roman_string[i + 1]] <= r_sym[roman_string[i]]:
                result += r_sym[roman_string[i]]
            else:
                result -= r_sym[roman_string[i]]
        else:
            result += r_sym[roman_string[i]]
    return result
