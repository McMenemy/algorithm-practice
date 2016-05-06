import string

def count_sort(magizine, query):
    buckets = dict.fromkeys(string.ascii_lowercase, 0)
    for char in magizine:
        if char != ' ':
            buckets[char] += 1

    for char in query:
        buckets[char] -= 1
        if buckets[char] < 0: return False

    return True

print(count_sort('hello there', 'hello'))
print(count_sort('peo afdaf', 'effd'))
print(count_sort('peo afdaf', 'efffd'))
