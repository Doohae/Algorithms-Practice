# 백준 - 염색체 9342
import re

N = int(input())
genes = []
for i in range(N):
    gene = input().split()
    genes.extend(gene)

# print(genes)
def infected(gene_string):
    infect = re.compile("(^[A-F]?A+F+C+[A-F]?$)")
    match = re.match(infect, gene_string)
    return bool(match)


for gene in genes:
    flag = infected(gene)
    if flag is True:
        print("Infected!")
    else:
        print("Good")

# /
# (^[A-F]?A+F+C+[A-F]?$)
# /
# gm
#
# 1st Capturing Group (^[A-F]?A+F+C+[A-F]?$)
# ^ asserts position at start of a line
#
# Match a single character present in the list below [A-F]
# ? matches the previous token between zero and one times, as many times as possible, giving back as needed (greedy)
# A-F matches a single character in the range between A (index 65) and F (index 70) (case sensitive)
#
# A matches the character A with index 6510 (4116 or 1018) literally (case sensitive)
#
# F matches the character F with index 7010 (4616 or 1068) literally (case sensitive)
#
# C matches the character C with index 6710 (4316 or 1038) literally (case sensitive)
#
# Match a single character present in the list below [A-F]
# ? matches the previous token between zero and one times, as many times as possible, giving back as needed (greedy)
# A-F matches a single character in the range between A (index 65) and F (index 70) (case sensitive)
# $ asserts position at the end of a line
#
# Global pattern flags
# g modifier: global. All matches (don't return after first match)
# m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)