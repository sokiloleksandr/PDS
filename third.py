alpha = ' abcdefghijklmnopqrstuvwxyz'
step=1
text =input("Please write your text ").strip()
res =""
for c in text:
    res += alpha[(alpha.index(c) +step)%len(alpha)]
print('Result: "' + res + '"')