a = 'ABCAAC1C'

def strcounter(a):
    for char in a :
        counter= 0
        for sub_char in a:
            if char == sub_char:
                counter+=1
        print(char,counter)

strcounter(a)

def strcounter(a):
    for char in set (a):
        counter = 0
        for sub_char in a:
            if char == sub_char:
                counter += 1
        print(char, counter)


def strcounter(a):
    syms_counter = {}
    for char in a:
        syms_counter[char] = syms_counter.get(char, 0)+1
    print(syms_counter)

    print(78)