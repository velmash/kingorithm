dial = input()

s = ['ABC', 'DEF', 'GHI', 'JKL', "MNO", "PQRS", "TUV", "WXYZ"]
num_list = []

for i in range(len(dial)):
    for j in range(len(s)):
        if dial[i] in s[j]:
            num_list.append(j+2)

print(sum(num_list) + len(num_list))