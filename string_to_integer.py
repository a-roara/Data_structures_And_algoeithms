def str_to_int(input_str):
    output_int = 0
    if input_str[0] == "-":
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        place = 10 ** (len(input_str) - (i + 1))
        digit = ord(input_str[i]) - ord("0")
        output_int += digit * place

    if is_negative:
        return -1 * output_int
    else:
        return output_int


print(str_to_int("-3456"))
print(type(str_to_int("3456")))
