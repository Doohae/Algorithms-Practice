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

# <[a-z 0-9]+>|[ a-zA-Z0-9]
# /
# gm
#
# 1st Alternative <[a-z 0-9]+>
# < matches the character < with index 6010 (3C16 or 748) literally (case sensitive)
#
# Match a single character present in the list below [a-z 0-9]
# + matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy)
# a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
#   matches the character   with index 3210 (2016 or 408) literally (case sensitive)
# 0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
# > matches the character > with index 6210 (3E16 or 768) literally (case sensitive)
#
# 2nd Alternative [ a-zA-Z0-9]
#
# Match a single character present in the list below [ a-zA-Z0-9]
#   matches the character   with index 3210 (2016 or 408) literally (case sensitive)
# a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
# A-Z matches a single character in the range between A (index 65) and Z (index 90) (case sensitive)
# 0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
#
# Global pattern flags
# g modifier: global. All matches (don't return after first match)
# m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)