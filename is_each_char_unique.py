# 3 ways of doing this
def normalize_str(str):
    str = str.replace(" ", "").lower()
    return str


# using dictionary
def method_1(str):
    str = normalize_str(str)
    ht = dict()

    for i in str:
        if i in ht:
            return False
        else:
            ht[i] = 1
    return True


# convert str to set
def method_2(str):
    return len(set(str)) == len(str)


# using alphabet string
def method_3(str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    str = normalize_str(str)
    for i in str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True


print(method_1("abcdefghij"))

print(method_2("abcdefaghijc"))

print(method_3("abcdefghijklc"))

