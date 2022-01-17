tel = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = list(input())
num = 0
for i in tel:
    for j in word:
        if j in i:
            num+= tel.index(i)+3
print(num)
