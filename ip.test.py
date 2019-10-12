stringResult = []
ipResult = []
# split = ['00000000', '00000100', '00000010', '00000001']
# string = split[0] + split[1] + split[2] + split[3]
string = input('Enter your number: ')

i = 4
while i > 0:
    str2 = string[:8]
    stringResult.append(str2)
    string = string.replace(str2, '', 1)
    # print(string)
    i -= 1

# print(string)
# print(stringResult)

i = 0
while i < 4:
    ips = int(stringResult[i], 2)
    stringIps = str(ips)
    ipResult.append(stringIps)
    # print(ips)
    i += 1

# print(ipResult)

print('Answer Is: ')
print(ipResult[0]+'.'+ipResult[1]+'.' + ipResult[2]+'.'+ipResult[3])
