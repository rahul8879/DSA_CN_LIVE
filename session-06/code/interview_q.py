def rev_pol_not(tokens):
    stack = []

    valid_operator = {
        '+': lambda n1, n2: n1 + n2,
        '-': lambda n1, n2: n1 - n2,
        '*': lambda n1, n2: n1 * n2,
        '/': lambda n1, n2: n1 / n2,
    }

    for token in tokens:
        if token in valid_operator:
            n2 = stack.pop()
            n1 = stack.pop()
            result = valid_operator[token](n1, n2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop() if stack else None


print(rev_pol_not(["2", "1", "+", "3", "*"]))  # Should print 9
print(rev_pol_not(["4", "13", "5", "/", "+"]))  # Should print 6

# invalid operator
print(rev_pol_not(["2", "1", "+", "3", "*", "+"]))  # Should print None