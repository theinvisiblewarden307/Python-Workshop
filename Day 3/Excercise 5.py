#Exercise: Summing numbers:

total = 0

for one_line in open('nums.txt'):
    if one_line.strip().isdigit():
        n = int(one_line)
        total += n

print(total)