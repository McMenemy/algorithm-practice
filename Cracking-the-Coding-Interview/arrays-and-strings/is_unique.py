import random

# runtime O(n), space O(n) could argue constant
def is_unique_chars(string):
    if len(string) > 128:
        return False

    char_dict = {}

    for char in string:
        if char in char_dict:
            return False

        char_dict[char] = 1

    return True

def string_sort(string):
    pivot_ind = random.randint(0, len(string) - 1)
    pivot = string[pivot_ind]
    left = ''
    right = ''

    for i, char in enumerate(string):
        if pivot_ind != i and char <= pivot:
            left += a
        elif pivot_ind != i and char > pivot:
            right += a

    return string_sort(left) + pivot + string_sort(right)

# runtime O(n), space O(n)  no new data structure
def is_unique_chars_2(string):
    sorted_string = string_sort(string)

    for i, char in enumerate(sorted_string[0:-1]):
        if char == sorted_string[i+1]:
            return False

    return True
 
unique_string = 'abcde'
non_unique_string = 'abcdae'

print(is_unique_chars(unique_string) == True)
print(is_unique_chars(non_unique_string) == False)

print(is_unique_chars_2(unique_string) == True)
print(is_unique_chars_2(non_unique_string) == False)
