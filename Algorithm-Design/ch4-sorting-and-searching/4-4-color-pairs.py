def color_pairs(color_list):
    red = []
    blue = []
    yellow = []
    for color_tuple in color_list:
        if color_tuple[1] == 'red':
            red.append(color_tuple)
        elif color_tuple[1] == 'blue':
            blue.append(color_tuple)
        elif color_tuple[1] == 'yellow':
            yellow.append(color_tuple)

    return red + blue + yellow

print(color_pairs([[1, 'blue'], [3, 'red'], [4, 'blue'], [6, 'yellow'], [9, 'red']]))
