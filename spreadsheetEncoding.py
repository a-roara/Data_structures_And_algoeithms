def spreadsheetEncoding(input_str):
    count = 0
    lenstr = len(input_str) - 1
    for i in range(len(input_str)):
        count += 26 ** lenstr * (ord(input_str[i]) - 64)
        lenstr -= 1
    return count


print(spreadsheetEncoding("ZZ"))

