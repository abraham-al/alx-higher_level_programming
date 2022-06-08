#!/usr/bin/python3
def best_score(a_dictionary):
    m = 0
    score = ""
    if a_dictionary:
        for i, j in a_dictionary.items():
            if j > m:
                score = i
                m = j
        return score
    else:
        return None
