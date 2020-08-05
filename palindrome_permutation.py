def palindrome_permutation(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    ht = dict()

    for i in input_str:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    odd_flag = 0

    for k, v in ht.items():
        if v % 2 != 0 and odd_flag == 0:
            odd_flag = 1
        elif v % 2 != 0 and odd_flag != 0:
            return False
    return True


print(palindrome_permutation("tacTt Coa"))

