s = ''
word = input("")
n = len(word) - 1
while n >= 0:
    s += word[n]
    n -= 1
print(s)