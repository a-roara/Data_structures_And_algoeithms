def isvowel(char):
    allvowels = "aeiou"
    return char in allvowels


def iterative(input_str):
    count = 0
    for i in range(len(input_str)):
        if isvowel(input_str[i]) == False:
            count += 1
    return count


def recursive(input_str):
    if len(input_str) == 0:
        return 0
    if isvowel(input_str[0]) == False:
        return 1 + recursive(input_str[1:])
    else:
        return recursive(input_str[1:])


str = "qwertuiagds"

print(iterative(str))
print(recursive(str))
