data = [[3,2,1],[1,2,1],[3,2,1]]

output = []
for i in data:
    sum = 0
    for j in i:
        sum += j
    output.append(sum)

print(output)
