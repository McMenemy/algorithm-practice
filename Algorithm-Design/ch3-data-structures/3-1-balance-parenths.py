def areParenthsBalanced(str):
    count = 0

    for char in str:
        if char == '(':
            count += 1

        if char == ')':
            count -= 1

        if count < 0:
            return False

    return count == 0

print areParenthsBalanced('((()))')
print areParenthsBalanced(')()')
print areParenthsBalanced('(()))')
