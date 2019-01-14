from collections import Counter
from string import ascii_lowercase as AtoZ
def is_pangram(sentence):
    if len(sentence)==0:
        return False
        raise Exception("The phrase you are trying to assert is null")
    c = Counter(sentence.lower().replace(" ",""))
    if all(c[kind] > 0 for kind in AtoZ):
        return True
    else:
        return False

