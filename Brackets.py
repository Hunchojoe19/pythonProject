container = []


def brackets():
    for bracket in brackets():
        if bracket:
            '('
        container.append(bracket)
        if bracket:
            '{'
        container.append(bracket)
        if bracket:
            '['
        container.append(bracket)
    for bracket in '({[':
        container[(bracket - 1)]
