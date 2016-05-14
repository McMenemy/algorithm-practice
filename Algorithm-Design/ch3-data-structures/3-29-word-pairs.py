def find_largest_word_pair(text):
    word_pair_dict = {}
    words = text.split(' ')
    greatest_count = 0
    greatest_word_pair = ''
    for i, word in enumerate(words[0:len(words) - 1]):
        word_pair = words[i] + ' ' + words[i+1]
        if word_pair in word_pair_dict:
            word_pair_dict[word_pair] += 1
        else:
            word_pair_dict[word_pair] = 1

        if word_pair_dict[word_pair] > greatest_count:
            greatest_count = word_pair_dict[word_pair]
            greatest_word_pair = word_pair

    return greatest_word_pair

print(find_largest_word_pair('I New York is a great city to live in. It is crowded with a bunch of rich people. I love New York City in New York'))
