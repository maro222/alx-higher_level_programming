#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence or sentence == "":
        mytuple = (0, None)
    else:
        mytuple = (len(sentence), sentence[i])
    return mytuple
