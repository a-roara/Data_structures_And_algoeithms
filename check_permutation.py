# two methods
# 1. sort and check each element. T.C - nlogn (because of sort) S.C - 1
# 2. use dictionaries. T.C - n S.C - n


def check_permutations(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = sorted(str1)
    str2 = sorted(str2)
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True


def check_permutations_2(str1, str2):
    ht = dict()
    if len(str1) != len(str2):
        return False

    for i in str1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in str2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for k, v in ht.items():
        if v != 0:
            return False
    return True


print(check_permutations("dog", "god"))

print(check_permutations("dog", "gos"))

print(check_permutations_2("dog", "god"))

print(check_permutations_2("google", "ooggle"))

