import sys

s = input()
pre_ls = [sys.maxsize] * len(s)
post_ls = [sys.maxsize] * len(s)
temp = 0
for i in range(len(s)):
    if s[i] == '1':
        temp += 1
    else:
        temp -= 1
    pre_ls[i] = min(0 if i == 0 else pre_ls[i - 1], temp)
temp = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == '1':
        temp += 1
    else:
        temp -= 1
    post_ls[i] = min(0 if i == len(s) - 1 else post_ls[i + 1], temp)
res = sum([1 for x in s if x == '0'])
temp = 0
for i in range(len(s)):
    temp = min(temp, max(-res, pre_ls[i] + post_ls[i]))
print(res + temp)

