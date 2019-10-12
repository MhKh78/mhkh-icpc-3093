# split = ['00000000', '00000100', '00000010', '00000001']
# string = split[0] + split[1] + split[2] + split[3]


def ipizer(string):
    stringResult = []
    ipResult = []
    i = 4
    while i > 0:
        str2 = string[:8]
        stringResult.append(str2)
        string = string.replace(str2, '', 1)
        i -= 1

    i = 0
    while i < 4:
        ips = int(stringResult[i], 2)
        stringIps = str(ips)
        ipResult.append(stringIps)
        i += 1

    print('Answer Is: ')
    print(ipResult[0]+'.'+ipResult[1]+'.' + ipResult[2]+'.'+ipResult[3])


print('Welcome to Ipizer')
n = int(input('Enter the N number: '))
inputs = []
while n > 0:
    inputs.append(input())
    n -= 1

for x in inputs:
    ipizer(x)
