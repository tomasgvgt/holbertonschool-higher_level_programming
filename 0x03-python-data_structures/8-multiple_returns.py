#!/usr/bin/python3


# Returns a tuple with the lenght and the first char of a string
def multiple_returns(sentence):
    if not sentence:
        return 0, None
    return len(sentence), sentence[0]
