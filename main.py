import names

menu = input('menu:'
            '\n1. Full name')

gender = input('chose gender: M/F')

def full_name(gender):

    if gender == 'M':
        full_n = names.get_full_name(gender='male')
    elif gender == 'F':
        full_n = names.get_full_name(gender='female')
    return full_n


full = full_name(gender)


if menu == '1':
    print(full)

else:
    print('please, print numbers 1-3')
