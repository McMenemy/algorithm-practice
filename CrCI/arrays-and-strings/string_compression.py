def string_compression(string):
    compressed_str = ''
    i = 0
    while i < len(string):
        current_letter = string[i]
        current_streak = 1
        while i < len(string) -1 and string[i+1] == current_letter:
            current_streak += 1
            i += 1

        compressed_str += current_letter + str(current_streak) 
        i += 1

    if len(string) < len(compressed_str):
        return string
    else:
        return compressed_str

print(string_compression('aabcccccaaa') == 'a2b1c5a3')
