def compare_equal_len_words(str1, str2):
    diffs = 0
    for i, char in enumerate(str1):
        if char != str2[i]:
            diffs += 1

        if diffs > 1:
            return False

    return True

def compare_unequal_len_words(longer_str, shorter_str):
    diffs = 0
    idx = 0

    for char in (shorter_str):
        if char != longer_str[idx]:
            diffs += 1
            idx += 1

        if diffs > 1:
            return False

        idx += 1

    return True

def one_away(str1, str2):

    if abs(len(str1) - len(str2)) >= 2:
        return False
    
    if len(str1) == len(str2):
        return compare_equal_len_words(str1, str2)
    elif len(str1) > len(str2):
        return compare_unequal_len_words(str1, str2)
    else:
        return compare_unequal_len_words(st2, str1)

print(one_away('pale', 'ple') == True)
print(one_away('pales', 'pale') == True)
print(one_away('pale', 'bale') == True)
print(one_away('pale', 'bake') == False)
