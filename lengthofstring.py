def lenstr_iterative(input_str):
    i = 0
    while 1:
        try:
            if input_str[i]:
                i += 1
        except:
            break
    return i


print(lenstr_iterative("asgfdgm"))


def lenstr_recursive(input_str, index=0):
    try:
        if input_str[index]:
            return lenstr_recursive(input_str, index + 1)
    except:
        return index


print(lenstr_recursive("asdreasdfghj"))

