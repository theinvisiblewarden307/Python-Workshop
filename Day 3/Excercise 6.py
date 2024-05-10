#Exercise: IP Addresses:

counts = {}

for one_line in open('mini-access-log.txt'):
    ip_address = one_line.split()[0]

    if ip_address in counts:      # if we've seen this address before
        counts[ip_address] += 1   # add 1 to its count
    else:
        counts[ip_address] = 1

for key, value in counts.items():
    print(f'{key}:\t{value}')


