from collections import defaultdict

def palindrome_permutation(string):
    char_counts = {}
    char_counts = defaultdict(lambda:0, char_counts)
    formatted_string = string.replace(" ", "").lower()

    for char in formatted_string:
        char_counts[char] += 1

    odd_count = 0
    even_count = 0

    for key, item in char_counts.items():
        if item % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if len(formatted_string) % 2 == 0:
        return odd_count == 0
    else:
        return odd_count == 1

print(palindrome_permutation('Tact Coa') == True)
print(palindrome_permutation('arg') == False)
