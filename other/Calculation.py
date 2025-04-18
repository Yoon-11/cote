n = int(input())

def calculation():
    sum = 0
    for _ in range(n):
        num_a, cal_chr, num_b = input().split()

        if cal_chr == '+':
            sum += int(num_a) + int(num_b)
        elif cal_chr == '-':
            sum += int(num_a) - int(num_b)
        elif cal_chr == '*':
            sum += int(num_a) * int(num_b)
        elif cal_chr == '/':
            sum += int(num_a) // int(num_b)

    return sum


result = calculation()
print(result)


