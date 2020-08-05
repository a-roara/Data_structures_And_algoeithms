def upper_case_recursive(input_str):
    if len(input_str) == 0:
        return 'no uppercase'
    if input_str[0].isupper():
        return input_str[0]
    else:
        return upper_case_recursive(input_str[1:])

print(upper_case_recursive('ujAasdjLaudgaiZ'))