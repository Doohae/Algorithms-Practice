import re

S = input()
def reverse_inside_tags(S):
    match = re.compile('<[a-z 0-9]+>|[ a-zA-Z0-9]')
    elems = re.findall(match, S)
    rev_full = ''
    rev_temp = ''
    for i, elem in enumerate(elems):
        if elem.startswith('<') or elem == ' ':
            rev_full += rev_temp[::-1]
            rev_temp = ''
            rev_full += elem
        elif i == len(elems)-1:
            rev_temp += elem
            rev_full += rev_temp[::-1]
        else:
            rev_temp += elem
    return rev_full

print(reverse_inside_tags(S))
