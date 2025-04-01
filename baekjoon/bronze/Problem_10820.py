import sys

for line in sys.stdin:
    s = line.rstrip('\n')

    if not s:
        break

    upper_count, lower_count, space_count, number_count = 0, 0, 0, 0

    for i in s:
        if i.isupper(): upper_count += 1
        elif i.islower() : lower_count += 1
        elif i.isdigit() : number_count += 1
        elif i.isspace() : space_count += 1

    print(lower_count, upper_count, number_count, space_count)


