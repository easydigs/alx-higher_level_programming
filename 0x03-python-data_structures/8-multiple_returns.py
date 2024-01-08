#!/usr/bin/python3
def multiple_returns(sentence):
    turple = ()
    if len(sentence) == 0:
        turple = 0, "None"
    else:
        turple = len(sentence), sentence[0]
    return (turple)
