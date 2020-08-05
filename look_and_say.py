def next_num_count(str_num):
    next_num = ""
    count = 1
    first_elem = str_num[0]
    for i in range(1, len(str_num)):
        if str_num[i - 1] == str_num[i]:
            count += 1
        else:
            next_num = next_num + str(count) + str_num[i - 1]
    next_num = next_num + str(count) + str_num[len(str_num) - 1]
    return next_num


def n_look_and_say(number):
    if number == 1:
        return "1"
    next_val = "1"
    for i in range(1, number):
        next_val = next_num_count(next_val)
    return next_val


print(n_look_and_say(2))
