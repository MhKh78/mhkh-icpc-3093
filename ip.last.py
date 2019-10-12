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

    print(ipResult[0]+'.'+ipResult[1]+'.' + ipResult[2]+'.'+ipResult[3])


n = int(input())
inputs = []
while n > 0:
    inputs.append(input())
    n -= 1

for x in inputs:
    ipizer(x)
