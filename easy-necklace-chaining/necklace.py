# https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

def same_necklace(string1, string2):
    same = True

    if(not validate(string1, string2)):
        return False
    
    combos = get_necklace_combos(string1)
    if((string2 not in combos) and string1 != ""):
       same = False        

    return same 

 # get the different combinations of string one and see if the string2 matches another 
def get_necklace_combos(string):
    combos = []

    for num in range (len(string)):
        new_combo = string[1:] + string[0]
        combos.append(new_combo)
        string = new_combo

    return combos


def validate(string1, string2):
    valid = True

    if(len(string1) != len(string2)):
        print("Number of characters mismatched")
        valid = False
    
    return valid

# TESTS

# print(get_necklace_combos("nicole"))

# print(same_necklace("nicole", "icolen")) # => true
# print(same_necklace("nicole", "lenico")) # => true
# print(same_necklace("nicole", "coneli")) # => false
# print(same_necklace("aabaaaaabaab", "aabaabaabaaa")) # => true
# print(same_necklace("abc", "cba")) # => false
# print(same_necklace("xxyyy", "xxxyy")) # => false
# print(same_necklace("xyxxz", "xxyxz")) # => false
# print(same_necklace("x", "x")) # => true
# print(same_necklace("x", "xx")) # => false
# print(same_necklace("x", "")) # => false
# print(same_necklace("", "")) # => true