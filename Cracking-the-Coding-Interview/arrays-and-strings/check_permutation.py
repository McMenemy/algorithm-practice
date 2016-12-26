from collections import defaultdict

# time O(n) space O(n)
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    char_counts = {}
    char_counts = defaultdict(lambda:0, char_counts)

    for char in str1:
        char_counts[char] += 1

    for char in str2:
        if char in char_counts:
            char_counts[char] -= 1
        else:
            return False

    return True

print(check_permutation('abbc', 'babc') == True)
print(check_permutation('abc', 'abbc') == False)
