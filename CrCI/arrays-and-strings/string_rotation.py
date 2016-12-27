def string_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    offset = -1

    for i, char in enumerate(str2):
        if char == str1[0]:
            offset = i

    if not offset:
        return False

    unrotated_str = ''
    wrapper = len(str2) - 1
    for i in range(offset, offset + len(str1)):
        unrotated_str += str2[i % len(str2)]

    return str1 == unrotated_str

print(string_rotation("waterbottle", "erbottlewat"))
