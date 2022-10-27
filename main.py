import names

menu = input('menu:'
            '\n1. Full name'
            '\n2. First name'
            '\n3. Last name \n')
gender = input('chose gender: M/F')

def full_name(gender):

    if gender == 'M':
        full_n = names.get_full_name(gender='male')
    elif gender == 'F':
        full_n = names.get_full_name(gender='female')
    return full_n

def first_name(gender):
    first_n = ''

    if gender == 'M':
        first_n = names.get_first_name(gender='male')
    elif gender == 'F':
        first_n = names.get_first_name(gender='female')
    return first_n

def last_name():
    last_n = names.get_last_name()
    return last_n

full = full_name(gender)
first = first_name(gender)
last = last_name()

if menu == '1':
    print(full)
elif menu == '2':
    print(first)
elif menu == '3':
    print(last)
else:
    print('please, print numbers 1-3')
